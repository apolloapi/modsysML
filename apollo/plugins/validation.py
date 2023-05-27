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

import io
import pathlib
import json

from tabulate import tabulate
from termcolor import colored, cprint
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from .utils import read_vars, read_prompts, evaluate, write_output
from apollo.manager import OpenAIConnectionManager


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

        self.args = self.parser.parse_args()
        self.provider = OpenAIConnectionManager()

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
            vars = read_vars(self.args.vars)

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
