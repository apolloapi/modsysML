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
import io
import pathlib
import json
import csv
import os

from time import sleep
from tqdm import tqdm
from tabulate import tabulate

from termcolor import colored, cprint
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from .utils import read_vars, read_prompts, write_output
from .evaluations import evaluate
from modsys.manager import ProviderConnectionManager


class PromptEngine(object):
    def __init__(self):
        self.parser = ArgumentParser(
            description="Evaluate data quality",
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
            help="One of: openai:<model name>, google_perspective:<model name> or path to custom API caller module",
        )
        self.parser.add_argument(
            "-o",
            "--output",
            type=pathlib.Path,
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
        self.parser.add_argument(
            "--eval",
            action="store_const",
            const="eval",
            default=None,
            help="Execute an evaluation job",
        )

        self.args = self.parser.parse_args()
        self.provider = ProviderConnectionManager()

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
        # Config
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

        # Vars
        vars = []
        if self.args.vars:
            vars = read_vars(
                self.args.vars,
                delimiter=self.args.delimiter if self.args.delimiter else ",",
            )

        # Providers
        providers = [self.provider.load_provider(p) for p in self.args.provider]

        options = {
            "prompts": read_prompts(self.args.prompt),
            "vars": vars,
            "providers": providers,
            **config,
        }

        # Evaluation
        summary = evaluate(options, providers[0])
        results = summary["results"]
        for j in tqdm(range(100), desc="Evaluation"):
            sleep(0.01)

        # Output
        if self.args.output:
            print_light_grey_on_yellow = lambda x: cprint(x, "black", "on_yellow")
            print_light_grey_on_yellow(f"Writing output to {self.args.output}")
            write_output(summary, output_path=self.args.output)
        else:
            # Output table by default
            print_light_grey_on_yellow = lambda x: cprint(x, "black", "on_yellow")
            print_light_grey_on_yellow("Writing output to table")
            write_output(results, output_path=None)

        print_yellow = lambda x: cprint(x, "yellow")
        print_yellow(f'Evaluation complete: {json.dumps(summary["stats"], indent=4)}')

    def setup(self):
        # function ran in cli.py at root
        if self.args.init == "init":
            self.init()
        elif self.args.eval == "eval":
            self.eval()
