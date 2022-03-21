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


class TestProjectVersion(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_project_versions(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}projects/TEST/versions",
            json=[
                {
                    "id": 1234567890,
                    "projectId": 1234567890,
                    "name": "wait for release",
                    "description": "",
                    "startDate": "2020-07-15T00:00:00Z",
                    "releaseDueDate": "2020-08-10T00:00:00Z",
                    "archived": False,
                    "displayOrder": 0
                },
            ],
            status=200
        )

        version = self.tested.get_project_versions("TEST")[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}projects/TEST/versions?apiKey=key")
        self.assertEqual(version.id, 1234567890)
        self.assertEqual(version.project_id, 1234567890)
        self.assertEqual(version.name, "wait for release")
        self.assertEqual(version.description, "")
        self.assertEqual(version.start_date, datetime(2020, 7, 15, 0, 0, 0))
        self.assertEqual(
            version.release_due_date, datetime(
                2020, 8, 10, 0, 0, 0))
        self.assertEqual(version.archived, False)
        self.assertEqual(version.display_order, 0)
