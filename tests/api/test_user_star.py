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


class TestUserStar(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_user_received_stars(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}users/1111111111/stars",
            json=[
                {
                    "id": 1234567890,
                    "comment": None,
                    "url": "https://xx.backlogtool.com/view/BLG-1",
                    "title": "[BLG-1] first issue | Show issue - Backlog",
                    "presenter": {
                        "id": 1,
                        "userId": "admin",
                        "name": "admin",
                        "roleType": 1,
                        "lang": "ja",
                        "mailAddress": "eguchi@nulab.example",
                        "nulabAccount": None,
                        "keyword": "Eguchi EGUCHI",
                    },
                    "created": "2014-01-23T10:55:19Z",
                },
            ],
            status=200)

        star = self.tested.get_user_received_stars(1111111111)[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}users/1111111111/stars?apiKey=key")
        self.assertEqual(star.id, 1234567890)
        self.assertEqual(star.comment, None)
        self.assertEqual(star.url, "https://xx.backlogtool.com/view/BLG-1")
        self.assertEqual(
            star.title,
            "[BLG-1] first issue | Show issue - Backlog")
        self.assertEqual(star.presenter.id, 1)
        self.assertEqual(star.presenter.user_id, "admin")
        self.assertEqual(star.presenter.name, "admin")
        self.assertEqual(star.presenter.role_type, 1)
        self.assertEqual(star.presenter.lang, "ja")
        self.assertEqual(star.presenter.mail_address, "eguchi@nulab.example")
        self.assertEqual(star.presenter.nulab_account, None)
        self.assertEqual(star.presenter.keyword, "Eguchi EGUCHI")
        self.assertEqual(star.created, datetime(2014, 1, 23, 10, 55, 19))

    @responses.activate
    def test_get_number_of_user_received_stars(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}users/1111111111/stars/count",
            json={
                "count": 54,
            },
            status=200)

        count = self.tested.get_number_of_user_received_stars(1111111111)

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}users/1111111111/stars/count?apiKey=key")
        self.assertEqual(count, 54)
