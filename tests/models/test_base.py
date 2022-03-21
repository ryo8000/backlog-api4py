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
from dataclasses import dataclass
from datetime import datetime

from backlog.models import Base


@dataclass
class TestClass(Base):
    id: int
    name: str
    data: dict
    updated: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=123,
            name="mike",
            data=data,
            updated=datetime.strptime(
                "2022-12-31T23:59:59Z",
                cls._DATETIME_FORMAT),
        )


class TestBase(unittest.TestCase):
    def setUp(self):
        self.tested = TestClass.from_dict({"key": "value"})

    def test_to_dict(self):
        base = self.tested.to_dict()

        self.assertEqual(
            base, {
                "id": 123,
                "name": "mike",
                "data": {"key": "value"},
                "updated": datetime(2022, 12, 31, 23, 59, 59)
            }
        )

    def test_to_json_string(self):
        base = self.tested.to_json_string()

        self.assertEqual(
            base,
            '{' +
            '"id": 123, ' +
            '"name": "mike", ' +
            '"data": {"key": "value"}, ' +
            '"updated": "2022-12-31T23:59:59Z"' +
            '}'
        )
