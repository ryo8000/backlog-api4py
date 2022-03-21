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


class TestPriority(unittest.TestCase):
    def setUp(self):
        self.tested = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

    @responses.activate
    def test_get_priorities(self):
        responses.add(
            responses.GET,
            f"{self.tested.base_url}priorities",
            json=[
                {
                    "id": 2,
                    "name": "High"
                },
                {
                    "id": 3,
                    "name": "Normal"
                },
                {
                    "id": 4,
                    "name": "Low"
                }
            ],
            status=200
        )

        resolutions = self.tested.get_priorities()

        request = responses.calls[0].request
        self.assertEqual(request.method, "GET")
        self.assertEqual(
            request.url,
            f"{self.tested.base_url}priorities?apiKey=key")
        self.assertEqual(resolutions[0].name, "HIGH")
        self.assertEqual(resolutions[0].to_value(), 2)
        self.assertEqual(resolutions[1].name, "NORMAL")
        self.assertEqual(resolutions[1].to_value(), 3)
        self.assertEqual(resolutions[2].name, "LOW")
        self.assertEqual(resolutions[2].to_value(), 4)
