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

"""File module."""

from dataclasses import dataclass
from datetime import datetime

from .base import Base
from .user import User


@dataclass
class Attachment(Base):
    """Attachment file class."""

    id: int
    name: str
    size: int
    created_user: User
    created: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            size=data["size"],
            created_user=User.from_dict(data["createdUser"]),
            created=datetime.strptime(data["created"], cls._DATETIME_FORMAT),
        )


@dataclass
class SharedFile(Base):
    """Shared file class."""

    id: int
    type: str
    dir: str
    name: str
    size: int
    created_user: User
    created: datetime
    updated_user: User
    updated: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            type=data["type"],
            dir=data["dir"],
            name=data["name"],
            size=data["size"],
            created_user=User.from_dict(data["createdUser"]),
            created=datetime.strptime(data["created"], cls._DATETIME_FORMAT),
            updated_user=User.from_dict(data["updatedUser"]),
            updated=datetime.strptime(data["updated"], cls._DATETIME_FORMAT),
        )
