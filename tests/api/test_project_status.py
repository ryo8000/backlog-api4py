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


class TestProjectStatus(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_project_statuses(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}projects/TEST/statuses",
            json=[
                {
                    "id": 1,
                    "projectId": 1234567890,
                    "name": "Open",
                    "color": "#ed8077",
                    "displayOrder": 1000
                },
            ],
            status=200
        )

        status = self.tested.get_project_statuses("TEST")[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}projects/TEST/statuses?apiKey=key")
        self.assertEqual(status.id, 1)
        self.assertEqual(status.project_id, 1234567890)
        self.assertEqual(status.name, "Open")
        self.assertEqual(status.color, "#ed8077")
        self.assertEqual(status.display_order, 1000)
