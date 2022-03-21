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

"""Star module."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base import Base
from .user import User


@dataclass
class Star(Base):
    """Star class."""

    id: int
    comment: Optional[str]
    url: str
    title: str
    presenter: User
    created: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            comment=data["comment"],
            url=data["url"],
            title=data["title"],
            presenter=User.from_dict(data["presenter"]),
            created=datetime.strptime(data["created"], cls._DATETIME_FORMAT),
        )
