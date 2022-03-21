# Copyright 2022 Ryo H
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import responses

from backlog import BacklogApi


class TestProjectUser(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_project_users(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}projects/TEST/users",
            json=[
                {
                    "id": 1234567890,
                    "userId": "mike.green@test.jp",
                    "name": "Mike Green",
                    "roleType": 2,
                    "lang": "ja",
                    "mailAddress": "mike.green@test.jp",
                    "nulabAccount": {
                        "nulabId": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn",
                        "name": "Mike Green",
                        "uniqueId": "mikegreen"},
                    "keyword": "Mike Green MIKEGREEN",
                }],
            status=200)

        user = self.tested.get_project_users("TEST")[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}projects/TEST/users?apiKey=key")
        self.assertEqual(user.id, 1234567890)
        self.assertEqual(user.user_id, "mike.green@test.jp")
        self.assertEqual(user.name, "Mike Green")
        self.assertEqual(user.role_type, 2)
        self.assertEqual(user.lang, "ja")
        self.assertEqual(user.mail_address, "mike.green@test.jp")
        self.assertEqual(user.nulab_account.nulab_id,
                         "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn")
        self.assertEqual(user.nulab_account.name, "Mike Green")
        self.assertEqual(user.nulab_account.unique_id, "mikegreen")
        self.assertEqual(user.keyword, "Mike Green MIKEGREEN")

    @responses.activate
    def test_get_project_administrators(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}projects/TEST/administrators",
            json=[
                {
                    "id": 1234567890,
                    "userId": "mike.green@test.jp",
                    "name": "Mike Green",
                    "roleType": 2,
                    "lang": "ja",
                    "mailAddress": "mike.green@test.jp",
                    "nulabAccount": {
                        "nulabId": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn",
                        "name": "Mike Green",
                        "uniqueId": "mikegreen"},
                    "keyword": "Mike Green MIKEGREEN",
                }],
            status=200)

        user = self.tested.get_project_administrators("TEST")[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}projects/TEST/administrators?apiKey=key")
        self.assertEqual(user.id, 1234567890)
        self.assertEqual(user.user_id, "mike.green@test.jp")
        self.assertEqual(user.name, "Mike Green")
        self.assertEqual(user.role_type, 2)
        self.assertEqual(user.lang, "ja")
        self.assertEqual(user.mail_address, "mike.green@test.jp")
        self.assertEqual(user.nulab_account.nulab_id,
                         "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn")
        self.assertEqual(user.nulab_account.name, "Mike Green")
        self.assertEqual(user.nulab_account.unique_id, "mikegreen")
        self.assertEqual(user.keyword, "Mike Green MIKEGREEN")
