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


def read_prompts(path):
    prompts = []
    for p in path:
        with open(p, "r") as f:
            content = f.read()
            items = content.split("---")
            prompts = list(item.strip() for item in items if item.strip())
    return prompts


def read_vars(path, delimiter):
    # Defaults to using csv vars file, support for json needed
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


def write_output(output_path, results, table=None):
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
