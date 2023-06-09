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

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="apollo-sdk",
    version="0.2.10",
    description="A radically simple framework for continuous ML validation and performance.",
    author="Apollo API",
    author_email="adrbrownx@gmail.com",
    packages=find_packages(),
    py_modules=["cli", "apollo"],
    url="https://github.com/apolloapi/apolloapi",
    license="Elastic License v2",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    platforms=["Any"],
    install_requires=requirements,
    long_description_content_type="text/markdown",
    long_description=long_description,
    entry_points={"console_scripts": ["apollo-sdk=cli:run_console"]},
)
