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
import io
import pathlib
import json
import csv
import os

from tabulate import tabulate
from termcolor import colored, cprint
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from .utils import read_vars, read_prompts, evaluate, write_output
from modsys.manager import OpenAIConnectionManager


class PromptEngine(object):
    def __init__(self):
        self.parser = ArgumentParser(
            description="Evaluate prompts",
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        self.parser.add_argument(
            "-p",
            "--prompt",
            type=pathlib.Path,
            action="append",
            help="Paths to prompt files (.txt)",
        )
        self.parser.add_argument(
            "-r",
            "--provider",
            type=str,
            action="append",
            help="One of: openai:chat, openai:completion, openai:<model name>, or path to custom API caller module",
        )
        self.parser.add_argument(
            "-o",
            "--output",
            type=str,
            help="Path to output file (csv, json, yaml)",
        )
        self.parser.add_argument(
            "-v",
            "--vars",
            type=pathlib.Path,
            help="Path to file with prompt variables (csv, json, yaml)",
        )
        self.parser.add_argument(
            "-c",
            "--config",
            type=pathlib.Path,
            help="Path to configuration file",
        )
        self.parser.add_argument(
            "-d",
            "--delimiter",
            type=pathlib.Path,
            help="Delimiter set in the vars file, defaults to [,]",
        )
        self.parser.add_argument(
            "--init",
            action="store_const",
            const="init",
            default=None,
            help="Initialize environment with configuration scripts",
        )

        self.args = self.parser.parse_args()
        self.provider = OpenAIConnectionManager()

    def init(self):
        config = {
            "provider": ["openai:completion"],
            "vars": "/vars.csv",
            "prompts": "/prompts.txt",
        }
        vars = [
            ["name", "question"],
            ["Tyler", "Can you help me find a specific product on your website?"],
            ["Jhon", "Do you have any promotions or discounts currently available?"],
            ["David", "What are your shipping and return policies?"],
            [
                "Adrian",
                "Can you provide more information about the product specifications or features?",
            ],
            [
                "User",
                "Can you recommend products that are similar to what I've been looking at?",
            ],
        ]
        prompts = [
            'Youre a chat assistant for a company. Answer this users question: {{name}}: "{{question}}"',
            'Youre a smart, bubbly chat assistant for a Trust & Safety team. Answer this users question: {{name}}: "{{question}}"',
        ]

        with open(os.path.join(os.getcwd(), f"prompts.txt"), "w") as f:
            f.write("\n--- \n".join(prompts))

        with open(
            os.path.join(os.getcwd(), f"vars.csv"), mode="w", newline=""
        ) as vars_file:
            writer = csv.writer(vars_file)
            writer.writerows(vars)

        with open(os.path.join(os.getcwd(), f"config.json"), "w") as f:
            json.dump(config, f)

    def eval(self):
        config_path = self.args.config
        config = {}
        if config_path:
            ext = pathlib.Path(config_path).suffix
            if ext == ".json":
                with io.open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
            # elif ext == '.py': # TODO: support yaml config files
            #     config = importlib.import_module(config_path)
            else:
                raise Error(f"Unsupported configuration file format: {ext}")

        vars = []
        if self.args.vars:
            vars = read_vars(
                self.args.vars,
                delimiter=self.args.delimiter if self.args.delimiter else ",",
            )

        providers = [self.provider.load_openai_provider(p) for p in self.args.provider]

        options = {
            "prompts": read_prompts(self.args.prompt),
            "vars": vars,  # NOTE: I think this is suppowed to be output not a path
            "providers": providers,
            **config,
        }

        # TODO update once you support multiple providers
        summary = evaluate(options, providers[0])
        results = summary["results"]
        if self.args.output:
            print_light_grey_on_yellow = lambda x: cprint(x, "black", "on_yellow")
            print_light_grey_on_yellow(f"Writing output to {self.args.output}")
            table_data = [
                [
                    result["prompt"][:60] + "..."
                    if len(result["prompt"]) > 60
                    else result["prompt"],
                    result["output"],
                    result.get("name", ""),
                    result["question"],
                ]
                for result in results
            ]
            write_output(self.args.output, summary["results"], summary["table"])
        else:
            # Output table by default
            headers = list(results[0].keys()) + ["state [pass/fail]"]
            print(headers)
            table_data = [
                [
                    result["prompt"][:60] + "..."
                    if len(result["prompt"]) > 60
                    else result["prompt"],
                    result["output"],
                    result.get("name", ""),
                    result["question"],
                ]
                for result in results
            ]
            num_headers = len(headers)
            min_width = 30
            max_width = 50

            # Calculate the width for each column based on the number of headers
            column_width = max(
                min_width, min(max_width, (max_width - min_width) // num_headers)
            )

            table = tabulate(
                table_data,
                headers=headers,
                # showindex="always",
                tablefmt="rounded_grid",
                maxcolwidths=column_width,
            )
            print(table)

        print_yellow = lambda x: cprint(x, "yellow")
        print_yellow(f'Evaluation complete: {json.dumps(summary["stats"], indent=4)}')

    def setup(self):
        if self.args.init == "init":
            self.init()
        else:
            self.eval()
