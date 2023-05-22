# Copyright 2022 Adrian Brown
# Copyright 2023 Apollo API, Inc.
#
#    Licensed under the Elastic License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         https://www.elastic.co/licensing/elastic-license
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
from jinja2 import Template
from tabulate import tabulate


# class Utilities:

#     def __init__(self, prompt_paths, vars_path):
#         # self.prompt_paths = prompt_paths
#         # self.vars_path = vars_path
#         self.vars_path = "vars.csv"
#         self.prompt_paths = "prompts.txt"


def read_prompts(self):  # allows you to work with multiple prompts
    prompts = []
    # for prompt_path in self.prompt_paths: FIXME
    with open(
        "/Users/abpyguru/Desktop/2023/apollo/apolloapi/apollo/module_utils/prompts.txt",
        "r",
    ) as f:
        prompts.extend(f.readlines())
    return prompts


def read_vars(self):

    # with open(self.vars_path, 'r') as f:
    with open(
        "/Users/abpyguru/Desktop/2023/apollo/apolloapi/apollo/module_utils/vars.csv",
        "r",
    ) as f:
        reader = csv.reader(f)
        return list(reader)


def write_output(self, output_path, results, table):
    output_extension = os.path.splitext(output_path)[1].lower()

    if output_extension == "csv":
        with open(output_path, "w") as f:
            writer = csv.writer(f)
            writer.writerows(table)
    elif output_extension == "json":
        with open(output_path, "w") as f:
            json.dump(results, f, indent=2)
    elif output_extension == "yaml":
        with open(output_path, "w") as f:
            yaml.dump(results, f)
    else:
        # if os.getenv('CLI') is not None:
        print(
            tabulate(
                table, headers=["Prompt", "Variables", "Result"], tablefmt="fancy_grid"
            )
        )
        # else:
        #     raise ValueError('Unsupported output file format. Use CSV, JSON, or YAML.')
