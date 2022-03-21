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
    def test_get_projects(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}projects",
            json=[
                {
                    "id": 1234567890,
                    "projectKey": "TEST",
                    "name": "test",
                    "chartEnabled": True,
                    "subtaskingEnabled": True,
                    "projectLeaderCanEditProjectLeader": False,
                    "useWikiTreeView": True,
                    "textFormattingRule": "markdown",
                    "archived": False,
                    "displayOrder": 1234567890,
                    "useDevAttributes": True,
                }
            ],
            status=200
        )

        project = self.tested.get_projects()[0]

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}projects?apiKey=key")
        self.assertEqual(project.id, 1234567890)
        self.assertEqual(project.project_key, "TEST")
        self.assertEqual(project.name, "test")
        self.assertEqual(project.chart_enabled, True)
        self.assertEqual(project.subtasking_enabled, True)
        self.assertEqual(project.project_leader_can_edit_project_leader, False)
        self.assertEqual(project.use_wiki_tree_view, True)
        self.assertEqual(project.text_formatting_rule, "markdown")
        self.assertEqual(project.archived, False)
        self.assertEqual(project.display_order, 1234567890)
        self.assertEqual(project.use_dev_attributes, True)

    @responses.activate
    def test_get_project(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}projects/TEST",
            json={
                "id": 1234567890,
                "projectKey": "TEST",
                "name": "test",
                "chartEnabled": True,
                "subtaskingEnabled": True,
                "projectLeaderCanEditProjectLeader": False,
                "useWikiTreeView": True,
                "textFormattingRule": "markdown",
                "archived": False,
                "displayOrder": 1234567890,
                "useDevAttributes": True,
            },
            status=200
        )

        project = self.tested.get_project("TEST")

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}projects/TEST?apiKey=key")
        self.assertEqual(project.id, 1234567890)
        self.assertEqual(project.project_key, "TEST")
        self.assertEqual(project.name, "test")
        self.assertEqual(project.chart_enabled, True)
        self.assertEqual(project.subtasking_enabled, True)
        self.assertEqual(project.project_leader_can_edit_project_leader, False)
        self.assertEqual(project.use_wiki_tree_view, True)
        self.assertEqual(project.text_formatting_rule, "markdown")
        self.assertEqual(project.archived, False)
        self.assertEqual(project.display_order, 1234567890)
        self.assertEqual(project.use_dev_attributes, True)
