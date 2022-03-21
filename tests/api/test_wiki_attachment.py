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


class TestWikiAttachment(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_wiki_attachments(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}wikis/1234567890/attachments",
            json=[
                {
                    "id": 1,
                    "name": "test.json",
                    "size": 8857,
                    "createdUser": {
                        "id": 1,
                        "userId": "admin",
                        "name": "admin",
                        "roleType": 1,
                        "lang": "ja",
                        "mailAddress": "eguchi@nulab.example"
                    },
                    "created": "2014-01-06T11:10:45Z"
                }
            ],
            status=200)

        attachment = self.tested.get_wiki_attachments(1234567890)[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}wikis/1234567890/attachments?apiKey=key")
        self.assertEqual(attachment.id, 1)
        self.assertEqual(attachment.name, "test.json")
        self.assertEqual(attachment.size, 8857)
        self.assertIsInstance(attachment.created_user, User)
        self.assertEqual(attachment.created, datetime(2014, 1, 6, 11, 10, 45))
