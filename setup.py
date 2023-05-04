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

setup(
    name="apollo-sdk",
    version="0.1.5",
    description="Build automated decision making workflows by aggregating your AI models and data into one api.",
    author="Apollo API, Inc.",
    author_email="adrbrownx@gmail.com",
    packages=find_packages(),
    # package_dir={'': ''},
    url="https://github.com/apolloapi/apolloapi",
    license="Elastic License v2",
    install_requires=[
        "Django==4.1.2",
        "firebase-admin==6.1.0",
        "grpcio==1.53.0",
        "httplib2==0.21.0",
        "protobuf==4.22.3",
        "psycopg2-binary==2.9.6",
        "python-dotenv==1.0.0",
        "psycopg==3.1.6",
        "requests==2.28.1",
        "psycopg2==2.9.3",
        "pytest==7.2.0",
        "PyJWT==2.6.0",
        "requests==2.28.1",
        "six==1.16.0",
        "sqlparse==0.4.3",
        "urllib3==1.26.13",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
