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

from jinja2 import Template, Environment, meta
from .grading import matches_expected_val


def evaluate(options, provider):
    results = []
    stats = {
        "successes": 0,
        "failures": 0,
        "error": [],
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
            provider_path = provider.id()
            path_parts = provider_path.split(":")
            model_name = path_parts[0]
            model_type = path_parts[1]

            if provider_path.startswith("openai:"):

                if vars[0].get("__expected"):
                    print(
                        "No support for test assertions from csv's for OpenAI provider"
                    )
                    raise NotImplementedError

                result = provider.call_api(rendered_prompt)
                results.append(
                    {
                        "prompt": prompt,
                        "output": result["output"],
                        **vars,
                    }
                )
                stats["tokenUsage"]["total"] += (
                    result["tokenUsage"].get("total", 0) or 0
                )
                stats["tokenUsage"]["prompt"] += (
                    result["tokenUsage"].get("prompt", 0) or 0
                )
                stats["tokenUsage"]["completion"] += (
                    result["tokenUsage"].get("completion", 0) or 0
                )
            elif provider_path.startswith("google_perspective:"):
                # NOTE default community_id and content_id's to modsysML since we
                # don't care about them for this use-case (testing). We only care
                # when it involves analyzing items for moderation and suggestions
                result = provider.call_api(
                    prompt=rendered_prompt,
                    community_id="ModsysML",
                    content_id="ModsysML",
                )

                # Find the score to compare against grade
                result = {
                    key: score["summaryScore"]["value"]
                    for key, score in result["attributeScores"].items()
                }
                ranking_value = max(result.values())
                ranking_key = max(k for k, v in result.items() if v == ranking_value)
                score = {ranking_key: {"value": ranking_value}}

                # Make comparison - default to model evaluation
                match = matches_expected_val(
                    vars["__expected"], score, options, comparison=vars["__comparison"]
                )

                # Update results
                results.append(
                    {
                        "prompt": rendered_prompt,
                        "output": score,
                        "passed": match,
                        **vars,
                    }
                )

                # Update evaluation stats
                stats["tokenUsage"]["prompt"] += 1
                stats["tokenUsage"]["completion"] += 1
                stats["tokenUsage"]["total"] += len(rendered_prompt.split())
            elif provider_path.startswith("sightengine:"):
                raise NotImplementedError

            stats["successes"] += 1
        except Exception as err:
            print("Error running evaluations, %s", err)
            stats["error"].append(err)
            stats["failures"] += 1
            raise err

    # Structure the rendered prompt for the run_eval method
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

    # NOTE: add a check to see if its a test by checking for __expected
    # Run evaluations
    for prompt_content, row in prompt_var_combinations:
        run_eval(prompt_content, row)

    return {
        "results": results,
        "stats": stats,
    }
