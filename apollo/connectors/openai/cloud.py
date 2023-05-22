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

import requests
import openai

from apollo.connectors.openai.base import AbstractApiProvider

# from typing import Any, Dict, List, Optional, Union


class OpenAiGenericProvider(AbstractApiProvider):
    model_name: str

    def __init__(self, model_name: str, api_key: str) -> None:
        super().__init__(api_key)
        self.model_name = model_name

    def id(self) -> str:
        return f"openai:{self.model_name}"

    def to_string(self) -> str:
        return f"[OpenAI Provider {self.model_name}]"

    def call_api(self, prompt: str):
        body = {
            "model": self.model_name,
            "prompt": prompt,
            "max_tokens": 1024,
            "temperature": 0,
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

            # import os

            # openai.api_key = os.getenv("OPENAI_API_KEY")

            # response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
        else:
            raise Exception(
                f"OpenAI API call failed with status code {response.json()}"
            )


class OpenAiCompletionProvider(OpenAiGenericProvider):
    def __init__(self, model_name: str, api_key: str) -> None:
        super().__init__(model_name, api_key)


class OpenAiChatCompletionProvider(OpenAiGenericProvider):
    def __init__(self, model_name: str, api_key: str) -> None:
        super().__init__(model_name, api_key)


# Will end up supporting universal models (google, aws, firestore, etc...)
def load_api_provider(provider_path: str):
    if provider_path.startswith("openai:"):
        path_parts = provider_path.split(":")
        model_type = path_parts[1]
        model_name = path_parts[2]
        if model_type == "chat":
            return OpenAiChatCompletionProvider(model_name or "gpt-3.5-turbo")
        elif model_type == "completion":
            return OpenAiCompletionProvider(model_name or "text-davinci-003")
        else:
            raise ValueError(f"Unknown OpenAI model type: {model_type}")
    else:
        return importlib.import_module(provider_path).default()
