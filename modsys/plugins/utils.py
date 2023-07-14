# Copyright: (c) 2022, Adrian Brown <adrbrownx@gmail.com>
# Copyright: (c) 2023, ModsysML Project
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
from tabulate import tabulate


def read_prompts(path, *args, **kwargs):
    prompts = []
    for p in path:
        with open(p, "r") as f:
            content = f.read()
            items = content.split("---")
            prompts = list(item.strip() for item in items if item.strip())
    return prompts


def read_vars(output_path, delimiter=None, *args, **kwargs):
    # Defaults to using csv vars file
    variables = []
    output_extension = os.path.splitext(output_path)[1].lower()
    if output_extension == ".csv":
        if delimiter is None:
            raise ValueError(
                "You haven't set delimiters for the csv vars file, do this using -d or --delimiter"
            )
        with open(output_path, "r") as f:
            reader = csv.reader(f, delimiter=delimiter)
            header = next(reader)  # skip the header elements
            for row in reader:
                if len(row) == len(
                    header
                ):  # Check if the row has the same number of elements as the header
                    variables.append(dict(zip(header, row)))
    elif output_extension == ".json":
        with open(output_path, "r") as f:
            variables = json.load(f)
    elif output_extension == ".yaml":
        raise NotImplementedError
    else:
        raise ValueError("Unsupported output file format. Use CSV or JSON.")

    return variables


def write_output(results, output_path=None, *args, **kwargs):
    output_extension = (
        os.path.splitext(output_path)[1].lower() if output_path is not None else None
    )
    summary = results
    results = results["results"]

    table_data = [
        [
            result["prompt"][:60] + "..."
            if len(result["prompt"]) > 60
            else result["prompt"],
            result["output"],
            result.get("__expected", ""),
            result.get("__comparison", ""),
            "pass" if result["passed"]["state"] else "fail",
        ]
        for result in results
    ]

    if output_extension is None:
        headers = list(results[0].keys()) + ["state [pass/fail]"]

        if results[0]["__expected"]:
            headers = [
                "prompt",
                "output",
                "expected",
                "comparison",
                "state [pass/fail]",
            ]

        print(headers)

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
    elif output_extension == ".csv":
        with open(output_path, "w") as f:
            writer = csv.writer(f)
            writer.writerows(table_data)
    elif output_extension == ".json":
        with open(output_path, "w") as f:
            r = json.dump(summary, f, indent=4)
    elif output_extension == ".yaml":
        with open(output_path, "w") as f:
            yaml.dump(summary, f)
    else:
        raise ValueError("Unsupported output file format. Use CSV, JSON, or YAML.")
