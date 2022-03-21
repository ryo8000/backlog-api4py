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
from backlog.models import Attachment, SharedFile, Star, User


class TestWiki(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_wikis(self):
        responses.add(responses.GET,
                      f"{self.tested.base_url}wikis",
                      json=[{"id": 1234567890,
                             "projectId": 1234567890,
                             "name": "Home",
                             "content": None,
                             "tags": [{"id": 12,
                                       "name": "proceedings"}],
                             "attachments": [{"id": 1,
                                              "name": "test.json",
                                              "size": 8857,
                                              "createdUser": {"id": 1,
                                                              "userId": "admin",
                                                              "name": "admin",
                                                              "roleType": 1,
                                                              "lang": "ja",
                                                              "mailAddress": "eguchi@nulab.example"},
                                              "created": "2014-01-06T11:10:45Z"}],
                             "sharedFiles": [{"id": 454403,
                                              "type": "file",
                                              "dir": "/userIcon/",
                                              "name": "01_male clerk.png",
                                              "size": 2735,
                                              "createdUser": {"id": 5686,
                                                              "userId": "takada",
                                                              "name": "takada",
                                                              "roleType": 2,
                                                              "lang": "ja",
                                                              "mailAddress": "takada@nulab.example"},
                                              "created": "2009-02-27T03:26:15Z",
                                              "updatedUser": {"id": 5686,
                                                              "userId": "takada",
                                                              "name": "takada",
                                                              "roleType": 2,
                                                              "lang": "ja",
                                                              "mailAddress": "takada@nulab.example"},
                                              "updated": "2009-03-03T16:57:47Z"}],
                             "stars": [{"id": 1234567890,
                                        "comment": None,
                                        "url": "https://xx.backlogtool.com/view/BLG-1",
                                        "title": "[BLG-1] first issue | Show issue - Backlog",
                                        "presenter": {"id": 1,
                                                      "userId": "admin",
                                                      "name": "admin",
                                                      "roleType": 1,
                                                      "lang": "ja",
                                                      "mailAddress": "eguchi@nulab.example",
                                                      },
                                        "created": "2014-01-23T10:55:19Z",
                                        }],
                             "createdUser": {"id": 1,
                                             "userId": "admin",
                                             "name": "admin",
                                             "roleType": 1,
                                             "lang": "ja",
                                             "mailAddress": "eguchi@nulab.example"},
                             "created": "2013-05-30T09:11:36Z",
                             "updatedUser": {"id": 1,
                                             "userId": "admin",
                                             "name": "admin",
                                             "roleType": 1,
                                             "lang": "ja",
                                             "mailAddress": "eguchi@nulab.example"},
                             "updated": "2013-05-30T09:11:36Z"}],
                      match=[responses.matchers.query_string_matcher("projectIdOrKey=TEST&apiKey=key")],
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
        self.assertIsInstance(wiki.attachments[0], Attachment)
        self.assertIsInstance(wiki.shared_files[0], SharedFile)
        self.assertIsInstance(wiki.stars[0], Star)
        self.assertIsInstance(wiki.created_user, User)
        self.assertEqual(wiki.created, datetime(2013, 5, 30, 9, 11, 36))
        self.assertIsInstance(wiki.updated_user, User)
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
            json={"id": 1234567890,
                  "projectId": 1234567890,
                  "name": "Home",
                  "content": None,
                  "tags": [{"id": 12,
                            "name": "proceedings"}],
                  "attachments": [{"id": 1,
                                   "name": "test.json",
                                   "size": 8857,
                                   "createdUser": {"id": 1,
                                                   "userId": "admin",
                                                   "name": "admin",
                                                   "roleType": 1,
                                                   "lang": "ja",
                                                   "mailAddress": "eguchi@nulab.example"},
                                   "created": "2014-01-06T11:10:45Z"}],
                  "sharedFiles": [{"id": 454403,
                                   "type": "file",
                                   "dir": "/userIcon/",
                                   "name": "01_male clerk.png",
                                   "size": 2735,
                                   "createdUser": {"id": 5686,
                                                   "userId": "takada",
                                                   "name": "takada",
                                                   "roleType": 2,
                                                   "lang": "ja",
                                                   "mailAddress": "takada@nulab.example"},
                                   "created": "2009-02-27T03:26:15Z",
                                   "updatedUser": {"id": 5686,
                                                   "userId": "takada",
                                                   "name": "takada",
                                                   "roleType": 2,
                                                   "lang": "ja",
                                                   "mailAddress": "takada@nulab.example"},
                                   "updated": "2009-03-03T16:57:47Z"}],
                  "stars": [{"id": 1234567890,
                             "comment": None,
                             "url": "https://xx.backlogtool.com/view/BLG-1",
                             "title": "[BLG-1] first issue | Show issue - Backlog",
                             "presenter": {"id": 1,
                                           "userId": "admin",
                                           "name": "admin",
                                           "roleType": 1,
                                           "lang": "ja",
                                           "mailAddress": "eguchi@nulab.example",
                                           },
                             "created": "2014-01-23T10:55:19Z",
                             }],
                  "createdUser": {"id": 1,
                                  "userId": "admin",
                                  "name": "admin",
                                  "roleType": 1,
                                  "lang": "ja",
                                  "mailAddress": "eguchi@nulab.example"},
                  "created": "2013-05-30T09:11:36Z",
                  "updatedUser": {"id": 1,
                                  "userId": "admin",
                                  "name": "admin",
                                  "roleType": 1,
                                  "lang": "ja",
                                  "mailAddress": "eguchi@nulab.example"},
                  "updated": "2013-05-30T09:11:36Z"},
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
        self.assertIsInstance(wiki.attachments[0], Attachment)
        self.assertIsInstance(wiki.shared_files[0], SharedFile)
        self.assertIsInstance(wiki.stars[0], Star)
        self.assertIsInstance(wiki.created_user, User)
        self.assertEqual(wiki.created, datetime(2013, 5, 30, 9, 11, 36))
        self.assertIsInstance(wiki.updated_user, User)
        self.assertEqual(wiki.updated, datetime(2013, 5, 30, 9, 11, 36))
