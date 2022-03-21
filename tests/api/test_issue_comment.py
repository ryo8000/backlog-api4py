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


class TestIssueComment(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_issue_comments(self):
        responses.add(responses.GET,
                      f"{self.tested.base_url}issues/1111111111/comments",
                      json=[{"id": 1234567890,
                             "content": "test",
                             "changeLog": [{"field": "priority",
                                            "newValue": "Normal",
                                            "originalValue": "High",
                                            "attachmentInfo": None,
                                            "attributeInfo": None,
                                            "notificationInfo": None,
                                            }],
                             "createdUser": {"id": 1,
                                             "userId": "admin",
                                             "name": "admin",
                                             "roleType": 1,
                                             "lang": "ja",
                                             "mailAddress": "eguchi@nulab.example"},
                             "created": "2013-08-05T06:15:06Z",
                             "updated": "2013-08-05T06:15:06Z",
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
                             "notifications": []},
                            ],
                      status=200)

        comment = self.tested.get_issue_comments(1111111111)[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}issues/1111111111/comments?apiKey=key")
        self.assertEqual(comment.id, 1234567890)
        self.assertEqual(comment.content, "test")
        self.assertEqual(comment.change_log[0].field, "priority")
        self.assertEqual(comment.change_log[0].new_value, "Normal")
        self.assertEqual(comment.change_log[0].original_value, "High")
        self.assertEqual(comment.change_log[0].attachment_info, None)
        self.assertEqual(comment.change_log[0].attribute_info, None)
        self.assertEqual(comment.change_log[0].notification_info, None)
        self.assertEqual(comment.created_user.id, 1)
        self.assertEqual(comment.created_user.user_id, "admin")
        self.assertEqual(comment.created_user.name, "admin")
        self.assertEqual(comment.created_user.role_type, 1)
        self.assertEqual(comment.created_user.lang, "ja")
        self.assertEqual(
            comment.created_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(comment.created, datetime(2013, 8, 5, 6, 15, 6))
        self.assertEqual(comment.updated, datetime(2013, 8, 5, 6, 15, 6))
        self.assertEqual(comment.stars[0].id, 1234567890)
        self.assertEqual(comment.stars[0].comment, None)
        self.assertEqual(
            comment.stars[0].url,
            "https://xx.backlogtool.com/view/BLG-1")
        self.assertEqual(
            comment.stars[0].title,
            "[BLG-1] first issue | Show issue - Backlog")
        self.assertEqual(comment.stars[0].presenter.id, 1)
        self.assertEqual(comment.stars[0].presenter.user_id, "admin")
        self.assertEqual(comment.stars[0].presenter.name, "admin")
        self.assertEqual(comment.stars[0].presenter.role_type, 1)
        self.assertEqual(comment.stars[0].presenter.lang, "ja")
        self.assertEqual(
            comment.stars[0].presenter.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(
            comment.stars[0].created, datetime(
                2014, 1, 23, 10, 55, 19))

    @responses.activate
    def test_get_number_of_comment(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}issues/1111111111/comments/count",
            json={
                "count": 54,
            },
            status=200)

        count = self.tested.get_number_of_comment(1111111111)

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}issues/1111111111/comments/count?apiKey=key")
        self.assertEqual(count, 54)

    @responses.activate
    def test_get_issue_comment(self):
        responses.add(responses.GET,
                      f"{self.tested.base_url}issues/1111111111/comments/2222222222",
                      json={"id": 1234567890,
                            "content": "test",
                            "changeLog": [{"field": "priority",
                                           "newValue": "Normal",
                                           "originalValue": "High",
                                           "attachmentInfo": None,
                                           "attributeInfo": None,
                                           "notificationInfo": None,
                                           }],
                            "createdUser": {"id": 1,
                                            "userId": "admin",
                                            "name": "admin",
                                            "roleType": 1,
                                            "lang": "ja",
                                            "mailAddress": "eguchi@nulab.example"},
                            "created": "2013-08-05T06:15:06Z",
                            "updated": "2013-08-05T06:15:06Z",
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
                            "notifications": []},
                      status=200)

        comment = self.tested.get_issue_comment(1111111111, 2222222222)

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}issues/1111111111/comments/2222222222?apiKey=key")
        self.assertEqual(comment.id, 1234567890)
        self.assertEqual(comment.content, "test")
        self.assertEqual(comment.change_log[0].field, "priority")
        self.assertEqual(comment.change_log[0].new_value, "Normal")
        self.assertEqual(comment.change_log[0].original_value, "High")
        self.assertEqual(comment.change_log[0].attachment_info, None)
        self.assertEqual(comment.change_log[0].attribute_info, None)
        self.assertEqual(comment.change_log[0].notification_info, None)
        self.assertEqual(comment.created_user.id, 1)
        self.assertEqual(comment.created_user.user_id, "admin")
        self.assertEqual(comment.created_user.name, "admin")
        self.assertEqual(comment.created_user.role_type, 1)
        self.assertEqual(comment.created_user.lang, "ja")
        self.assertEqual(
            comment.created_user.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(comment.created, datetime(2013, 8, 5, 6, 15, 6))
        self.assertEqual(comment.updated, datetime(2013, 8, 5, 6, 15, 6))
        self.assertEqual(comment.stars[0].id, 1234567890)
        self.assertEqual(comment.stars[0].comment, None)
        self.assertEqual(
            comment.stars[0].url,
            "https://xx.backlogtool.com/view/BLG-1")
        self.assertEqual(
            comment.stars[0].title,
            "[BLG-1] first issue | Show issue - Backlog")
        self.assertEqual(comment.stars[0].presenter.id, 1)
        self.assertEqual(comment.stars[0].presenter.user_id, "admin")
        self.assertEqual(comment.stars[0].presenter.name, "admin")
        self.assertEqual(comment.stars[0].presenter.role_type, 1)
        self.assertEqual(comment.stars[0].presenter.lang, "ja")
        self.assertEqual(
            comment.stars[0].presenter.mail_address,
            "eguchi@nulab.example")
        self.assertEqual(
            comment.stars[0].created, datetime(
                2014, 1, 23, 10, 55, 19))
