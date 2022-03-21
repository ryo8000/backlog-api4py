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

"""Issue module."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from .base import Base


@dataclass
class Status(Base):
    """Status class."""

    id: int
    project_id: int
    name: str
    color: str
    display_order: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            project_id=data["projectId"],
            name=data["name"],
            color=data["color"],
            display_order=data["displayOrder"],
        )


@dataclass
class IssueType(Base):
    """Issue Type class."""

    id: int
    project_id: int
    name: str
    color: str
    display_order: int
    template_summary: Optional[str]
    template_description: Optional[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            project_id=data["projectId"],
            name=data["name"],
            color=data["color"],
            display_order=data["displayOrder"],
            template_summary=data.get("templateSummary"),
            template_description=data.get("templateDescription"),
        )


@dataclass
class Category(Base):
    """Category class."""

    id: int
    name: str
    display_order: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            name=data["name"],
            display_order=data["displayOrder"],
        )


@dataclass
class Version(Base):
    """Versions(Milestones) class."""

    id: int
    project_id: int
    name: str
    description: Optional[str]
    start_date: Optional[datetime]
    release_due_date: Optional[datetime]
    archived: bool
    display_order: int

    @classmethod
    def from_dict(cls, data: dict):
        start_date = datetime.strptime(
            data["startDate"],
            cls._DATETIME_FORMAT) if data["startDate"] else None
        release_due_date = datetime.strptime(
            data["releaseDueDate"],
            cls._DATETIME_FORMAT) if data["releaseDueDate"] else None

        return cls(
            id=data["id"],
            project_id=data["projectId"],
            name=data["name"],
            description=data["description"],
            start_date=start_date,
            release_due_date=release_due_date,
            archived=data["archived"],
            display_order=data["displayOrder"],
        )
