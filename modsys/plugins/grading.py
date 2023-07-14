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

import json

DEFAULT_SEVERITY_SIMILARITY_THRESHOLD = 0.89


# NOTE: add in robust type checks and organize logic
def matches_expected_val(expected, output, options, *args, **kwargs):
    provider = options["providers"][0]
    provider_path = provider.id()

    # str inference tells us we should check to see if we're running a non-eval grading system
    if type(expected) == str:
        if expected.startswith("def:"):
            raise NotImplementedError
        elif expected.startswith("grade:"):
            raise NotImplementedError
        elif expected.startswith("semantic:"):
            raise NotImplementedError

    # eval: or no prefix specified this option comes with an optional
    # __comprision variable as well.
    if provider_path.startswith("google_perspective:"):
        # Update expected if we're running eval: so that way we can format
        # a dict to pull its value
        if type(expected) == str:
            expected = json.loads(expected)

        comparison = kwargs["comparison"] if "comparison" in kwargs else None
        output_dict = list(output.values())
        output_value = round(output_dict[0]["value"] * 100, 2)
        expected_dict = list(expected.values())
        expected_value = round(float(expected_dict[0]["value"]) * 100, 2)

        if comparison == "<":
            boolean = expected_value < output_value
        elif comparison == "<=":
            boolean = expected_value <= output_value
        elif comparison == ">=":
            boolean = expected_value >= output_value
        elif comparison == ">":
            boolean = expected_value > output_value
        else:
            raise ValueError("Unsupported assertion, use <: <=: >: or >=:")
    elif provider_path.startswith("openai:"):
        raise NotImplementedError
    elif provider_path.startswith("sightengine:"):
        raise NotImplementedError
    else:
        raise NotImplementedError

    return {
        "state": boolean,
        "reason": f"Expected {expected} {comparison} {output}",
    }
