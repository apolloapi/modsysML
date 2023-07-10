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

import requests
import openai
import os

from modsys.connectors.openai.base import AbstractOpenAIProvider


class OpenAiGenericProvider(AbstractOpenAIProvider):
    temp_val = os.environ.get("OPENAI_TEMPERATURE", 0)
    max_token_val = os.environ.get("OPENAI_MAX_TOKENS", 1024)
    api_key_val = os.environ.get("OPENAI_API_KEY", None)

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.api_key = self.api_key_val
        self.tokens = int(self.max_token_val)
        self.temp = int(self.temp_val)

    def id(self) -> str:
        return f"openai:{self.model_name}"

    def to_string(self) -> str:
        return f"[OpenAI Provider {self.model_name}]"

    def token_settings(self) -> str:
        return f"Using {self.tokens} tokens"

    def temp_settings(self) -> str:
        return f"Temp set to {self.temp}"

    def call_api(self, prompt: str):
        body = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": self.tokens,
            "temperature": self.temp,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        response = requests.post(
            "https://api.openai.com/v1/completions", headers=headers, json=body
        )
        if response.status_code == 200:
            data = response.json()
            return {
                "output": data["choices"][0]["text"],
                "tokenUsage": {
                    "total": data["usage"]["total_tokens"],
                    "prompt": data["usage"]["prompt_tokens"],
                    "completion": data["usage"]["completion_tokens"],
                },
            }
        else:
            raise Exception(
                f"OpenAI API call failed with status code {response.json()}"
            )
