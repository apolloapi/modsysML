#!/usr/bin/env python

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

# from tabulate import Table
# from termcolor import Fore, Style
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

# from logger import logger
# from providers import load_api_provider
# from evaluator import evaluate
# from util import read_prompts, read_vars, write_output
from utils import read_vars, read_prompts

# from types import CommandLineOptions, EvaluateOptions, VarMapping


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

    def foo(self):
        print(self.args)

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
            # print(config)

        vars = []
        if self.args.vars:
            vars = read_vars(self.args.vars)
        # print(vars)

        # providers = [load_api_provider(p) for p in self.args.provider]  # NOTE: in progress
        options = {
            "prompts": read_prompts(self.args.prompt),
            "vars": vars,  # NOTE: I think this is suppowed to be output not a path
            # 'providers': providers,
            **config,
        }
        # print(options)

        # summary = await evaluate(options)

        # if self.args.output:
        #     logger.info(Fore.YELLOW(f'Writing output to {self.args.output}'))
        #     write_output(self.args.output, summary.results, summary.table)
        # else:
        #     # Output table by default
        #     max_width = sys.stdout.columns if sys.stdout.columns else 120
        #     head = summary.table[0]
        #     table = Table( # NOTE use tabulate here
        #         head,
        #         col_widths=list(map(lambda x: math.floor(max_width / len(x)), head)),
        #         word_wrap=True,
        #         wrap_on_word_boundary=True,
        #     )
        #     table.add_rows(summary.table[1:])
        #     logger.info(table.table)

        # logger.info(Fore.GREEN + Style.BRIGHT(f'Evaluation complete: {json.dumps(summary.stats, indent=2)}'))
        # logger.info('Done.')


if __name__ == "__main__":
    program = PromptEngine()
    program.foo()
    program.eval()
