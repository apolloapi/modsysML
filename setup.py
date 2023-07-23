#!/usr/bin/env python

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

from setuptools import setup, find_packages
from modsys.const import BASE_DIR

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="modsys",
    version="0.5.0",
    description="A radically simple framework for ML/AI model management",
    author="ModsysML",
    author_email="adrbrownx@gmail.com",
    packages=find_packages(),
    py_modules=["cli", "modsys"],
    url="https://github.com/modsysML/modsys",
    license="Apache License, Version 2.0",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    platforms=["Any"],
    install_requires=[
        "Django>3.0",
        "firebase-admin==6.2.0",
        "google-api-core==2.11.1",
        "google-api-python-client==2.92.0",
        "google-auth==2.21.0",
        "google-auth-httplib2==0.1.0",
        "google-cloud-core==2.3.3",
        "google-cloud-firestore==2.11.1",
        "google-cloud-storage==2.10.0",
        "google-crc32c==1.5.0",
        "google-resumable-media==2.5.0",
        "googleapis-common-protos==1.59.1",
        "Jinja2==3.1.2",
        "openai==0.27.7",
        "psycopg==3.1.6",
        "psycopg-binary==3.1.6",
        "psycopg-pool==3.1.7",
        "psycopg2-binary==2.9.6",
        "python-dotenv==1.0.0",
        "requests==2.28.1",
        "tabulate==0.9.0",
        "termcolor==2.3.0",
        "tqdm==4.65.0",
        "virtualenv==20.21.0",
    ],
    long_description_content_type="text/markdown",
    long_description=long_description,
    entry_points={"console_scripts": ["modsys=cli:run_console"]},
)
