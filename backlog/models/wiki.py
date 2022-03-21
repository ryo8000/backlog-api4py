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

"""Wiki module."""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from .base import Base
from .file import Attachment, SharedFile
from .star import Star
from .user import User


@dataclass
class Tag(Base):
    """Tag class."""

    id: int
    name: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
        )


@dataclass
class Wiki(Base):
    """Wiki class."""

    id: int
    project_id: int
    name: str
    content: Optional[str]
    tags: List[Tag]
    attachments: List[Attachment]
    shared_files: List[SharedFile]
    stars: List[Star]
    created_user: User
    created: datetime
    updated_user: User
    updated: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            project_id=data["projectId"],
            name=data["name"],
            content=data["content"],
            tags=[Tag.from_dict(t) for t in data["tags"]],
            attachments=[Attachment.from_dict(a) for a in data["attachments"]],
            shared_files=[SharedFile.from_dict(s) for s in data["sharedFiles"]],
            stars=[Star.from_dict(s) for s in data["stars"]],
            created_user=User.from_dict(data["createdUser"]),
            created=datetime.strptime(data["created"], cls._DATETIME_FORMAT),
            updated_user=User.from_dict(data["updatedUser"]),
            updated=datetime.strptime(data["updated"], cls._DATETIME_FORMAT),
        )
