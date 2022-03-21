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


class TestWiki(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_wikis(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}wikis",
            json=[
                {
                    "id": 1234567890,
                    "projectId": 1234567890,
                    "name": "Home",
                    "content": None,
                    "tags": [
                        {
                            "id": 12,
                            "name": "proceedings"
                        }
                    ],
                    "attachments": [
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
                    "sharedFiles": [
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
                    "stars": [],
                    "createdUser": {
                        "id": 1,
                        "userId": "admin",
                        "name": "admin",
                        "roleType": 1,
                        "lang": "ja",
                        "mailAddress": "eguchi@nulab.example"},
                    "created": "2013-05-30T09:11:36Z",
                    "updatedUser": {
                        "id": 1,
                        "userId": "admin",
                        "name": "admin",
                        "roleType": 1,
                        "lang": "ja",
                        "mailAddress": "eguchi@nulab.example"},
                    "updated": "2013-05-30T09:11:36Z"
                }
            ],
            match=[
                responses.matchers.query_string_matcher(
                    "projectIdOrKey=TEST&apiKey=key")
            ],
            status=200)

        wiki = self.tested.get_wikis("TEST")[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}wikis?projectIdOrKey=TEST&apiKey=key")
        self.assertEqual(wiki.id, 1234567890)
        self.assertEqual(wiki.project_id, 1234567890)
        self.assertEqual(wiki.name, "Home")
        self.assertEqual(wiki.content, None)
        self.assertEqual(wiki.tags[0].id, 12)
        self.assertEqual(wiki.tags[0].name, "proceedings")
        self.assertEqual(wiki.attachments[0].id, 1)
        self.assertEqual(wiki.attachments[0].name, "test.json")
        self.assertEqual(wiki.attachments[0].size, 8857)
        self.assertEqual(wiki.attachments[0].created_user.id, 1)
        self.assertEqual(
            wiki.attachments[0].created_user.user_id,
            "admin")
        self.assertEqual(wiki.attachments[0].created_user.name, "admin")
        self.assertEqual(wiki.attachments[0].created_user.role_type, 1)
        self.assertEqual(wiki.attachments[0].created_user.lang, "ja")
        self.assertEqual(
            wiki.attachments[0].created_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(
            wiki.attachments[0].created, datetime(
                2014, 1, 6, 11, 10, 45))
        self.assertEqual(wiki.shared_files[0].id, 454403)
        self.assertEqual(wiki.shared_files[0].type, "file")
        self.assertEqual(wiki.shared_files[0].dir, "/userIcon/")
        self.assertEqual(wiki.shared_files[0].name, "01_male clerk.png")
        self.assertEqual(wiki.shared_files[0].size, 2735)
        self.assertEqual(wiki.shared_files[0].created_user.id, 5686)
        self.assertEqual(
            wiki.shared_files[0].created_user.user_id,
            "takada")
        self.assertEqual(wiki.shared_files[0].created_user.name, "takada")
        self.assertEqual(wiki.shared_files[0].created_user.role_type, 2)
        self.assertEqual(wiki.shared_files[0].created_user.lang, "ja")
        self.assertEqual(
            wiki.shared_files[0].created_user.mail_address,
            "takada@nulab.example")
        self.assertEqual(
            wiki.shared_files[0].created, datetime(
                2009, 2, 27, 3, 26, 15))
        self.assertEqual(wiki.shared_files[0].updated_user.id, 5686)
        self.assertEqual(
            wiki.shared_files[0].updated_user.user_id,
            "takada")
        self.assertEqual(wiki.shared_files[0].updated_user.name, "takada")
        self.assertEqual(wiki.shared_files[0].updated_user.role_type, 2)
        self.assertEqual(wiki.shared_files[0].updated_user.lang, "ja")
        self.assertEqual(
            wiki.shared_files[0].updated_user.mail_address,
            "takada@nulab.example")
        self.assertEqual(
            wiki.shared_files[0].updated, datetime(
                2009, 3, 3, 16, 57, 47))
        self.assertEqual(wiki.stars, [])
        self.assertEqual(wiki.created_user.id, 1)
        self.assertEqual(wiki.created_user.user_id, "admin")
        self.assertEqual(wiki.created_user.name, "admin")
        self.assertEqual(wiki.created_user.role_type, 1)
        self.assertEqual(wiki.created_user.lang, "ja")
        self.assertEqual(
            wiki.created_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(wiki.updated, datetime(2013, 5, 30, 9, 11, 36))
        self.assertEqual(wiki.updated_user.id, 1)
        self.assertEqual(wiki.updated_user.user_id, "admin")
        self.assertEqual(wiki.updated_user.name, "admin")
        self.assertEqual(wiki.updated_user.role_type, 1)
        self.assertEqual(wiki.updated_user.lang, "ja")
        self.assertEqual(
            wiki.updated_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(wiki.updated, datetime(2013, 5, 30, 9, 11, 36))

    @responses.activate
    def test_get_number_of_wikis(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}wikis/count",
            json={
                "count": 5,
            },
            match=[
                responses.matchers.query_string_matcher(
                    "projectIdOrKey=TEST&apiKey=key")
            ],
            status=200)

        count = self.tested.get_number_of_wikis("TEST")

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}wikis/count?projectIdOrKey=TEST&apiKey=key")
        self.assertEqual(count, 5)

    @responses.activate
    def test_get_wiki(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}wikis/1234567890",
            json={
                "id": 1234567890,
                "projectId": 1234567890,
                "name": "Home",
                "content": None,
                "tags": [
                        {
                            "id": 12,
                            "name": "proceedings"
                        }
                ],
                "attachments": [
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
                "sharedFiles": [
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
                "stars": [],
                "createdUser": {
                    "id": 1,
                    "userId": "admin",
                    "name": "admin",
                    "roleType": 1,
                    "lang": "ja",
                    "mailAddress": "eguchi@nulab.example"},
                "created": "2013-05-30T09:11:36Z",
                "updatedUser": {
                    "id": 1,
                    "userId": "admin",
                    "name": "admin",
                    "roleType": 1,
                    "lang": "ja",
                    "mailAddress": "eguchi@nulab.example"},
                "updated": "2013-05-30T09:11:36Z"
            },
            status=200)

        wiki = self.tested.get_wiki(1234567890)

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}wikis/1234567890?apiKey=key")
        self.assertEqual(wiki.id, 1234567890)
        self.assertEqual(wiki.project_id, 1234567890)
        self.assertEqual(wiki.name, "Home")
        self.assertEqual(wiki.content, None)
        self.assertEqual(wiki.tags[0].id, 12)
        self.assertEqual(wiki.tags[0].name, "proceedings")
        self.assertEqual(wiki.attachments[0].id, 1)
        self.assertEqual(wiki.attachments[0].name, "test.json")
        self.assertEqual(wiki.attachments[0].size, 8857)
        self.assertEqual(wiki.attachments[0].created_user.id, 1)
        self.assertEqual(
            wiki.attachments[0].created_user.user_id,
            "admin")
        self.assertEqual(wiki.attachments[0].created_user.name, "admin")
        self.assertEqual(wiki.attachments[0].created_user.role_type, 1)
        self.assertEqual(wiki.attachments[0].created_user.lang, "ja")
        self.assertEqual(
            wiki.attachments[0].created_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(
            wiki.attachments[0].created, datetime(
                2014, 1, 6, 11, 10, 45))
        self.assertEqual(wiki.shared_files[0].id, 454403)
        self.assertEqual(wiki.shared_files[0].type, "file")
        self.assertEqual(wiki.shared_files[0].dir, "/userIcon/")
        self.assertEqual(wiki.shared_files[0].name, "01_male clerk.png")
        self.assertEqual(wiki.shared_files[0].size, 2735)
        self.assertEqual(wiki.shared_files[0].created_user.id, 5686)
        self.assertEqual(
            wiki.shared_files[0].created_user.user_id,
            "takada")
        self.assertEqual(wiki.shared_files[0].created_user.name, "takada")
        self.assertEqual(wiki.shared_files[0].created_user.role_type, 2)
        self.assertEqual(wiki.shared_files[0].created_user.lang, "ja")
        self.assertEqual(
            wiki.shared_files[0].created_user.mail_address,
            "takada@nulab.example")
        self.assertEqual(
            wiki.shared_files[0].created, datetime(
                2009, 2, 27, 3, 26, 15))
        self.assertEqual(wiki.shared_files[0].updated_user.id, 5686)
        self.assertEqual(
            wiki.shared_files[0].updated_user.user_id,
            "takada")
        self.assertEqual(wiki.shared_files[0].updated_user.name, "takada")
        self.assertEqual(wiki.shared_files[0].updated_user.role_type, 2)
        self.assertEqual(wiki.shared_files[0].updated_user.lang, "ja")
        self.assertEqual(
            wiki.shared_files[0].updated_user.mail_address,
            "takada@nulab.example")
        self.assertEqual(
            wiki.shared_files[0].updated, datetime(
                2009, 3, 3, 16, 57, 47))
        self.assertEqual(wiki.stars, [])
        self.assertEqual(wiki.created_user.id, 1)
        self.assertEqual(wiki.created_user.user_id, "admin")
        self.assertEqual(wiki.created_user.name, "admin")
        self.assertEqual(wiki.created_user.role_type, 1)
        self.assertEqual(wiki.created_user.lang, "ja")
        self.assertEqual(
            wiki.created_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(wiki.updated, datetime(2013, 5, 30, 9, 11, 36))
        self.assertEqual(wiki.updated_user.id, 1)
        self.assertEqual(wiki.updated_user.user_id, "admin")
        self.assertEqual(wiki.updated_user.name, "admin")
        self.assertEqual(wiki.updated_user.role_type, 1)
        self.assertEqual(wiki.updated_user.lang, "ja")
        self.assertEqual(
            wiki.updated_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(wiki.updated, datetime(2013, 5, 30, 9, 11, 36))
