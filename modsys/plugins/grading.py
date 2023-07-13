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

DEFAULT_SEVERITY_SIMILARITY_THRESHOLD = 0.89


def matches_expected_val(expected, output, options):
    if expected.startswith("def:"):
        raise NotImplementedError
    elif expected.startswith("grade:"):
        raise NotImplementedError
    elif expected.startswith("semantic:"):
        raise NotImplementedError
    else:
        if options == ">=" or options == ">":
            boolean = expected >= output
        elif options == "<=" or options == "<":
            boolean = expected <= output

        return {
            "pass": boolean,
            "reason": f"Expected {expected} but the output is {output}",
        }
