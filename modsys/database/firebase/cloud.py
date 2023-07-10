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

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from modsys.exceptions import FirebaseConnectionError
from modsys.database.firebase.base import AbstractFirebaseClient
from modsys.const import TEST_ACCOUNT


# https://firebase.google.com/docs/admin/setup?authuser=0#python
class FirebaseClient(AbstractFirebaseClient):
    def __init__(self, service_account_key):
        self.project_id = None
        self.database_url = None
        self.service_account_key = service_account_key

    def init_with_service_account(self):
        """
        Initialize the Firestore DB client using a service account
        :param file_path: path to service account
        :return: firestore
        """
        # cred = credentials.Certificate(self.service_account_key) FIXME:
        cred = credentials.Certificate(TEST_ACCOUNT)
        try:
            firebase_admin.initialize_app(cred)
            return firestore.client()
        except Exception as err:
            raise FirebaseConnectionError(err)

    def init_with_project_id(self):
        """
        Initialize the Firestore DB client using a GCP project ID
        :param project_id: The GCP project ID
        :return: firestore
        """
        # cred = credentials.ApplicationDefault()
        app_options = {"projectId": self.project_id}
        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(options=app_options)
        return firestore.client()

    def init_with_database_url(self):
        cred = credentials.Certificate(self.service_account_key)
        try:
            firebase_admin.initialize_app(cred, {"databaseURL": self.database_url})
            return firestore.client()
        except Exception as err:
            raise FirebaseConnectionError(err)

    def close(self):
        # NOTE can check for live connections as well: firebase_admin._apps)
        firebase_admin.delete_app(firebase_admin.get_app())

    # TODO: add custom exception and return a custom warning
    def execute(self, collection_name):
        if not self.service_account_key:
            return

        try:
            cursor = self.init_with_service_account()
        except:
            raise ValueError

        response = [
            item.to_dict()
            for item in cursor.collection(collection_name).limit(10).get()
        ]
        self.close()

        return response

    # TODO: add custom exception and return a custom warning
    def list_tables(self):
        if not self.service_account_key:
            return

        try:
            cursor = self.init_with_service_account()
        except:
            raise ValueError

        collections = [collection.id for collection in cursor.collections()]
        self.close()

        return collections
