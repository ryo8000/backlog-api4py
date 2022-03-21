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
from datetime import datetime

import responses

from backlog import BacklogApi
from backlog.models import User


class TestWikiSharedFile(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_wiki_shared_files(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}wikis/1234567890/sharedFiles",
            json=[
                {
                    "id": 454403,
                    "type": "file",
                    "dir": "/userIcon/",
                    "name": "01_male clerk.png",
                    "size": 2735,
                    "createdUser": {
                        "id": 5686,
                        "userId": "takada",
                        "name": "takada",
                        "roleType": 2,
                        "lang": "ja",
                        "mailAddress": "takada@nulab.example"
                    },
                    "created": "2009-02-27T03:26:15Z",
                    "updatedUser": {
                        "id": 5686,
                        "userId": "takada",
                        "name": "takada",
                        "roleType": 2,
                        "lang": "ja",
                        "mailAddress": "takada@nulab.example"
                    },
                    "updated": "2009-03-03T16:57:47Z"
                }
            ],
            status=200)

        shared_file = self.tested.get_wiki_shared_files(1234567890)[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}wikis/1234567890/sharedFiles?apiKey=key")

        self.assertEqual(shared_file.id, 454403)
        self.assertEqual(shared_file.type, "file")
        self.assertEqual(shared_file.dir, "/userIcon/")
        self.assertEqual(shared_file.name, "01_male clerk.png")
        self.assertEqual(shared_file.size, 2735)
        self.assertIsInstance(shared_file.created_user, User)
        self.assertEqual(shared_file.created, datetime(2009, 2, 27, 3, 26, 15))
        self.assertIsInstance(shared_file.updated_user, User)
        self.assertEqual(shared_file.updated, datetime(2009, 3, 3, 16, 57, 47))
