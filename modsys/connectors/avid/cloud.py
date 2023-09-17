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

from modsys.connectors.avid.base import AbstractAVIDProvider

from datetime import datetime
import json

current_date = datetime.now()


class AVIDProvider(AbstractAVIDProvider):
    def __init__(self):
        self.report = None
        self.status = None

    def create_report(
        self,
        provider_name,
        provider_model,
        dataset_name,
        dataset_link,
        summary,
        path_to_save_report,
    ):
        report_format = {
            "data_type": "AVID",
            "data_version": None,
            "metadata": None,
            "affects": {
                "developer": [],
                "deployer": [str(provider_name)],
                "artifacts": [{"type": "Model", "name": str(provider_model)}],
            },
            "problemtype": {
                "classof": "LLM Evaluation",
                "type": "Detection",
                "description": {"lang": "eng", "value": str(summary)},
            },
            "metrics": [],
            "references": [{"label": str(dataset_name), "url": str(dataset_link)}],
            "description": {"lang": "eng", "value": str(summary)},
            "impact": {
                "avid": {
                    "risk_domain": ["Performance"],
                    "sep_view": ["P0102: Accuracy"],
                    "lifecycle_view": ["L05: Evaluation"],
                    "taxonomy_version": "0.2",
                }
            },
            "credit": "ModsysML",
            "reported_date": current_date.strftime("%Y-%m-%d"),
        }

        # Serialize the report dictionary to JSON
        report_json = json.dumps(report_format, indent=4)

        # Write the JSON to the specified file
        with open(path_to_save_report, "w") as json_file:
            json_file.write(report_json)

        return "Report created."
