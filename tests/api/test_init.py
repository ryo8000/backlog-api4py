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

from backlog import (
    BacklogApi
)


class TestBacklogApiInit(unittest.TestCase):
    def test_space_key_is_invalid(self):
        with self.assertRaises(ValueError):
            BacklogApi(
                space_key="",
                space_type="jp",
                api_key="key",
            )

    def test_space_type_is_jp(self):
        api = BacklogApi(
            space_key="test",
            space_type="jp",
            api_key="key",
        )

        self.assertEqual(api.base_url, "https://test.backlog.jp/api/v2/")
        self.assertEqual(api.api_key, "key")

    def test_space_type_is_com(self):
        api = BacklogApi(
            space_key="test",
            space_type="com",
            api_key="key",
        )

        self.assertEqual(api.base_url, "https://test.backlog.com/api/v2/")
        self.assertEqual(api.api_key, "key")

    def test_space_type_is_tool(self):
        api = BacklogApi(
            space_key="test",
            space_type="tool",
            api_key="key",
        )

        self.assertEqual(api.base_url, "https://test.backlogtool.com/api/v2/")
        self.assertEqual(api.api_key, "key")

    def test_space_type_is_invalid(self):
        with self.assertRaises(ValueError):
            BacklogApi(
                space_key="test",
                space_type="",
                api_key="key",
            )

    def test_api_key_is_invalid(self):
        with self.assertRaises(ValueError):
            BacklogApi(
                space_key="test",
                space_type="jp",
                api_key="",
            )
