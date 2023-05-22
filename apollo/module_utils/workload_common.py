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

# Eval function
import jinja2


def evaluate(options: EvaluateOptions) -> EvaluateSummary:
    prompts = []
    results = []

    for prompt_content in options.prompts:
        for provider in options.providers:
            prompts.append(
                {
                    "content": prompt_content,
                    "display": (
                        # options.providers.length > 1
                        # ? f"[{provider.id()}] {prompt_content}"
                        # : prompt_content,
                    ),
                }
            )

    table = [
        [
            *prompts.map(lambda p: p.display),
            *Object.keys(options.vars or {}),
        ],
    ]

    stats = {
        "successes": 0,
        "failures": 0,
        "token_usage": {
            "total": 0,
            "prompt": 0,
            "completion": 0,
        },
    }

    # async def run_eval(
    #     options: RunEvalOptions,
    # ) -> Optional[str]:
    #     vars = options.vars or {}
    #     template = jinja2.Template(options.prompt)
    #     rendered_prompt = template.render(vars)

    #     try:
    #         result = await options.provider.call_api(rendered_prompt)
    #         row = {
    #             "prompt": (
    #                 # options.include_provider_id
    #                 # ? f"[{options.provider.id()}] {options.prompt}"
    #                 # : options.prompt,
    #             ),
    #             "output": result.output,
    #             "vars": vars,
    #         }
    #         results.append(row)

    #         stats["successes"] += 1
    #         stats["token_usage"]["total"] += result.token_usage.total or 0
    #         stats["token_usage"]["prompt"] += result.token_usage.prompt or 0
    #         stats["token_usage"]["completion"] += result.token_usage.completion or 0
    #         return result.output
    #     except Exception as err:
    #         stats["failures"] += 1
    #         return str(err)

    # vars = options.vars or [{}]
    # for row in vars:
    #     outputs = []
    #     for prompt_content in options.prompts:
    #         for provider in options.providers:
    #             output = await run_eval({
    #                 "provider": provider,
    #                 "prompt": prompt_content,
    #                 "vars": row,
    #                 "include_provider_id": options.providers.length > 1,
    #             })
    #             outputs.append(output)

    #     # Set up table headers: Prompt 1, Prompt 2, ..., Prompt N, Var 1 name, Var 2 name, ..., Var N name
    #     # And then table rows: Output 1, Output 2, ..., Output N, Var 1 value, Var 2 value, ..., Var N value
    #     table.append([*outputs, *Object.values(row)])

    return {
        "results": results,
        "stats": stats,
        "table": table,
    }


# # index function

# from evaluator import evaluate as do_evaluate
# from providers import load_api_provider

# from typing import List, Optional, Union


# def evaluate(
#     providers,
#     options,
# ):
#     """Evaluates prompts using the specified providers.

#     Args:
#         providers: The providers to use. Can be a string, a list of strings, or a list of `ApiProvider` objects.
#         options: Optional keyword arguments to pass to the `evaluate` function.

#     Returns:
#         An `EvaluateSummary` object containing the results of the evaluation.
#     """

#     if not options:
#         options = {}

#     api_providers = []

#     if isinstance(providers, str):
#         api_providers.append(load_api_provider(providers))
#     elif isinstance(providers, list):
#         for provider in providers:
#             if isinstance(provider, str):
#                 api_providers.append(load_api_provider(provider))
#             else:
#                 api_providers.append(provider)
#     else:
#         raise ValueError(f"providers must be a string, a list of strings, or a list of ApiProvider objects, but got {providers!r}")

#     return do_evaluate(options, api_providers)
