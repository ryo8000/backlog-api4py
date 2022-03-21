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


class TestSpace(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_space(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}space",
            json={
                "spaceKey": "test",
                "name": "Test Inc.",
                "ownerId": 1234567890,
                "lang": "ja",
                "timezone": "Asia/Tokyo",
                "reportSendTime": "09:00:00",
                "textFormattingRule": "backlog",
                "created": "2013-01-01T00:00:00Z",
                "updated": "2022-12-31T23:59:59Z",
            },
            status=200
        )

        space = self.tested.get_space()

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}space?apiKey=key")
        self.assertEqual(space.space_key, "test")
        self.assertEqual(space.name, "Test Inc.")
        self.assertEqual(space.owner_id, 1234567890)
        self.assertEqual(space.lang, "ja")
        self.assertEqual(space.timezone, "Asia/Tokyo")
        self.assertEqual(space.report_send_time, "09:00:00")
        self.assertEqual(space.text_formatting_rule, "backlog")
        self.assertEqual(space.created, datetime(2013, 1, 1, 0, 0, 0))
        self.assertEqual(space.updated, datetime(2022, 12, 31, 23, 59, 59))
