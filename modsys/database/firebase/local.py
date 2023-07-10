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

from modsys.database.firebase.base import AbstractFirebaseClient


class FakeFirebaseClient(AbstractFirebaseClient):
    def execute(self, nosql):
        pass

    def init_with_service_account(self):
        """
        Initialize the Firestore DB client using a service account
        :param file_path: path to service account
        :return: firestore
        """

    def init_with_project_id(self):
        """
        Initialize the Firestore DB client using a GCP project ID
        :param project_id: The GCP project ID
        :return: firestore
        """

    def init_with_database_url(self):
        pass

    def close():
        pass

    def execute(self, nosql):
        pass

    def execute(self, collection_name):
        pass

    def list_tables(self):
        pass
