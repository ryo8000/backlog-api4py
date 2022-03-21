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


class TestProject(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_project_issue_types(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}projects/TEST/issueTypes",
            json=[
                {
                    "id": 1234567890,
                    "projectId": 1234567890,
                    "name": "Bug",
                    "color": "#990000",
                    "displayOrder": 0,
                    "templateSummary": "Subject",
                    "templateDescription": "Description",
                },
            ],
            status=200
        )

        issue_type = self.tested.get_project_issue_types("TEST")[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}projects/TEST/issueTypes?apiKey=key")
        self.assertEqual(issue_type.id, 1234567890)
        self.assertEqual(issue_type.project_id, 1234567890)
        self.assertEqual(issue_type.name, "Bug")
        self.assertEqual(issue_type.color, "#990000")
        self.assertEqual(issue_type.display_order, 0)
        self.assertEqual(issue_type.template_summary, "Subject")
        self.assertEqual(issue_type.template_description, "Description")
