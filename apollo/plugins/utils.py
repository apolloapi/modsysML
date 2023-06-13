# Copyright 2023 Apollo API, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import csv
import json
import yaml
from tqdm import tqdm
from jinja2 import Template, Environment, meta
from tabulate import tabulate


def read_prompts(path):
    prompts = []
    for p in path:
        with open(p, "r") as f:
            content = f.read()
            items = content.split("---")
            prompts = list(item.strip() for item in items if item.strip())
    return prompts


def read_vars(path, delimiter):
    variables = []
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=delimiter)
        header = next(reader)  # skip the header elements
        for row in reader:
            if len(row) == len(
                header
            ):  # Check if the row has the same number of elements as the header
                variables.append(dict(zip(header, row)))
    return variables


def write_output(output_path, results, table):
    output_extension = os.path.splitext(output_path)[1].lower()
    if output_extension == ".csv":
        with open(output_path, "w") as f:
            writer = csv.writer(f)
            writer.writerows(table)
    if output_extension == ".json":
        with open(output_path, "w") as f:
            r = json.dump(results, f, indent=4)
    elif output_extension == ".yaml":
        with open(output_path, "w") as f:
            yaml.dump(results, f)
    # else: TODO: test this
    # if os.getenv('CLI') is not None:
    # print(
    #     tabulate(
    #         table, headers=["Prompt", "Variables", "Result"], tablefmt="fancy_grid"
    #     )
    # )
    # else:
    #     raise ValueError('Unsupported output file format. Use CSV, JSON, or YAML.')


def evaluate(options, provider):
    results = []
    stats = {
        "successes": 0,
        "failures": 0,
        "tokenUsage": {
            "total": 0,
            "prompt": 0,
            "completion": 0,
        },
    }

    def run_eval(prompt, vars):

        # Setup template and check for vars to connect prompt
        vars = vars if vars else {}
        template = Template(prompt)
        env = Environment()
        undeclared_vars = meta.find_undeclared_variables(env.parse(prompt))
        context = {variable: vars.get(variable) for variable in undeclared_vars}
        rendered_prompt = (
            template.render(context) if undeclared_vars else template.render()
        )

        try:
            result = provider.call_api(rendered_prompt)

            results.append(
                {
                    "prompt": prompt,
                    "output": result["output"],
                    **vars,
                }
            )

            stats["successes"] += 1
            stats["tokenUsage"]["total"] += result["tokenUsage"].get("total", 0) or 0
            stats["tokenUsage"]["prompt"] += result["tokenUsage"].get("prompt", 0) or 0
            stats["tokenUsage"]["completion"] += (
                result["tokenUsage"].get("completion", 0) or 0
            )
        except Exception as err:
            stats["failures"] += 1

    if options["vars"]:
        prompt_var_combinations = [
            (prompt_content, row)
            for row in options["vars"]
            for prompt_content in options["prompts"]
        ]
    else:
        prompt_var_combinations = [
            (prompt_content, {}) for prompt_content in options["prompts"]
        ]

    total_evaluations = len(prompt_var_combinations)
    with tqdm(total=total_evaluations, desc="Evaluating", unit="evaluation") as pbar:
        for i, (prompt_content, row) in enumerate(prompt_var_combinations):
            run_eval(prompt_content, row)
            pbar.update(1)
            # # Generate a random number between 1 and 10
            # random_increment = random.randint(1, 10)

            # # Increment the progress bar by the random number
            # pbar.update(random_increment)

            # If it's the last iteration, update the progress bar to reach 100
            # if i == total_evaluations - 1:
            #     remaining = total_evaluations - (pbar.n - random_increment)
            #     pbar.update(remaining)

    return {
        "results": results,
        "stats": stats,
    }
