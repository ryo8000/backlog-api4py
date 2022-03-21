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

"""Backlog API module."""

from typing import List, Optional, Union

import requests

from .models import (Attachment, Category, Comment, IssueType, Priority,
                     Project, Resolution, Space, Star, Status, User, Version,
                     Wiki)


class BacklogApi(object):
    """Backlog API class."""

    SPACE_TYPES = {
        "jp": "backlog.jp",
        "com": "backlog.com",
        "tool": "backlogtool.com"
    }

    def __init__(self, space_key: str, space_type: str, api_key: str):
        """__init__ method.

        :param space_key: space key
        :param space_type: space type
        :param api_key: api key
        :raises ValueError: when initialization fails
        """
        if not space_key:
            raise ValueError("space_key must not be empty.")
        domain = self.SPACE_TYPES.get(space_type)
        if not domain:
            raise ValueError("space_type must be one of 'jp', 'com', 'tool'.")
        if not api_key:
            raise ValueError("api_key must not be empty.")

        self.base_url = f"https://{space_key}.{domain}/api/v2/"
        self.api_key = api_key

    def get_space(self) -> Space:
        """Get information about your space.

        :return: space information
        """
        url = "space"

        space = self._send_get_request(url)
        return Space.from_dict(space)

    def get_users(self) -> List[User]:
        """Get list of users in your space.

        :return: list of users
        """
        url = "users"

        users = self._send_get_request(url)
        return [User.from_dict(user) for user in users]

    def get_user(self, user_id: int) -> User:
        """Get information about user.

        :param user_id: user id
        :return: user information
        """
        url = f"users/{user_id}"

        user = self._send_get_request(url)
        return User.from_dict(user)

    def get_own_user(self) -> User:
        """Get own information about user.

        :return: user information
        """
        url = "users/myself"

        user = self._send_get_request(url)
        return User.from_dict(user)

    def get_user_received_stars(self, user_id: int) -> List[Star]:
        """Get list of stars that user received.

        :param user_id: user id
        :return: list of stars
        """
        url = f"users/{user_id}/stars"

        stars = self._send_get_request(url)
        return [Star.from_dict(star) for star in stars]

    def get_number_of_user_received_stars(self, user_id: int) -> int:
        """Get number of stars that user received.

        :param user_id: user id
        :return: number of stars
        """
        url = f"users/{user_id}/stars/count"

        res = self._send_get_request(url)
        return res["count"]

    def get_priorities(self) -> List[Priority]:
        """Get list of priorities that can be set for issue.

        :return: list of priorities
        """
        url = "priorities"

        priorities = self._send_get_request(url)
        return [Priority.value_of(priority["id"]) for priority in priorities]

    def get_resolutions(self) -> List[Resolution]:
        """Get list of resolutions that can be set for issue.

        :return: list of resolutions
        """
        url = "resolutions"

        resolutions = self._send_get_request(url)
        return [Resolution.value_of(resolution["id"])
                for resolution in resolutions]

    def get_projects(self) -> List[Project]:
        """Get list of projects.

        :return: list of projects
        """
        url = "projects"

        projects = self._send_get_request(url)
        return [Project.from_dict(project) for project in projects]

    def get_project(self, project_id_or_key: Union[int, str]) -> Project:
        """Get information about project.

        :param project_id_or_key: project id or project key
        :return: project information
        """
        url = f"projects/{project_id_or_key}"

        project = self._send_get_request(url)
        return Project.from_dict(project)

    def get_project_users(
            self, project_id_or_key: Union[int, str]) -> List[User]:
        """Get list of project members.

        :param project_id_or_key: project id or project key
        :return: list of project members
        """
        url = f"projects/{project_id_or_key}/users"

        users = self._send_get_request(url)
        return [User.from_dict(user) for user in users]

    def get_project_administrators(
            self, project_id_or_key: Union[int, str]) -> List[User]:
        """Get list of users who has project administrator role.

        :param project_id_or_key: project id or project key
        :return: list of project administrators
        """
        url = f"projects/{project_id_or_key}/administrators"

        administrators = self._send_get_request(url)
        return [User.from_dict(administrator)
                for administrator in administrators]

    def get_project_statuses(
            self, project_id_or_key: Union[int, str]) -> List[Status]:
        """Get list of statuses in the project.

        :param project_id_or_key: project id or project key
        :return: list of issue statuses
        """
        url = f"projects/{project_id_or_key}/statuses"

        statuses = self._send_get_request(url)
        return [Status.from_dict(status) for status in statuses]

    def get_project_issue_types(
            self, project_id_or_key: Union[int, str]) -> List[IssueType]:
        """Get list of issue types in the project.

        :param project_id_or_key: project id or project key
        :return: list of issue types
        """
        url = f"projects/{project_id_or_key}/issueTypes"

        issue_types = self._send_get_request(url)
        return [IssueType.from_dict(issue_type) for issue_type in issue_types]

    def get_project_categories(
            self, project_id_or_key: Union[int, str]) -> List[Category]:
        """Get list of categories in the project.

        :param project_id_or_key: project id or project key
        :return: list of categories
        """
        url = f"projects/{project_id_or_key}/categories"

        categories = self._send_get_request(url)
        return [Category.from_dict(category) for category in categories]

    def get_project_versions(
            self, project_id_or_key: Union[int, str]) -> List[Version]:
        """Get list of versions(milestones) in the project.

        :param project_id_or_key: project id or project key
        :return: list of versions(milestones)
        """
        url = f"projects/{project_id_or_key}/versions"

        versions = self._send_get_request(url)
        return [Version.from_dict(version) for version in versions]

    def get_issue_comments(
            self, issue_id_or_key: Union[int, str]) -> List[Comment]:
        """Get list of comments in issue.

        :param issue_id_or_key: issue id or issue key
        :return: list of comments
        """
        url = f"issues/{issue_id_or_key}/comments"

        comments = self._send_get_request(url)
        return [Comment.from_dict(comment) for comment in comments]

    def get_number_of_comments(
            self, issue_id_or_key: Union[int, str]) -> int:
        """Get number of comments in issue.

        :param issue_id_or_key: issue id or issue key
        :return: number of comments
        """
        url = f"issues/{issue_id_or_key}/comments/count"

        res = self._send_get_request(url)
        return res["count"]

    def get_issue_comment(
            self,
            issue_id_or_key: Union[int, str],
            comment_id: int) -> Comment:
        """Get information about comment.

        :param issue_id_or_key: issue id or issue key
        :param comment_id: comment id
        :return: list of comments
        """
        url = f"issues/{issue_id_or_key}/comments/{comment_id}"

        comment = self._send_get_request(url)
        return Comment.from_dict(comment)

    def get_wikis(
            self,
            project_id_or_key: Union[int, str],
            keyword: Optional[str] = None) -> List[Wiki]:
        """Get list of wiki pages.

        :param project_id_or_key: project id or project key
        :param keyword: keyword
        :return: list of wiki pages
        """
        url = "wikis"
        query_params = {
            "projectIdOrKey": project_id_or_key,
        }
        if keyword is not None:
            query_params["keyword"] = keyword

        wikis = self._send_get_request(url, query_params)
        return [Wiki.from_dict(wiki) for wiki in wikis]

    def get_number_of_wikis(
            self, project_id_or_key: Union[int, str]) -> int:
        """Get number of wiki pages.

        :param project_id_or_key: project id or project key
        :return: number of wiki pages
        """
        url = "wikis/count"
        query_params = {
            "projectIdOrKey": project_id_or_key,
        }

        res = self._send_get_request(url, query_params)
        return res["count"]

    def get_wiki(self, wiki_id: int) -> Wiki:
        """Get information about wiki page.

        :param wiki_id: wiki id
        :return: list of wiki pages
        """
        url = f"wikis/{wiki_id}"

        wiki = self._send_get_request(url)
        return Wiki.from_dict(wiki)

    def get_wiki_attachments(
            self,
            wiki_id: int) -> List[Attachment]:
        """Get list of files attached to wiki.

        :param wiki_id: wiki id
        :return: list of wiki attachments
        """
        url = f"wikis/{wiki_id}/attachments"

        wikis = self._send_get_request(url)
        return [Attachment.from_dict(wiki) for wiki in wikis]

    def _send_get_request(self, path: str, query_params: dict = None):
        query_params = query_params or {}
        query_params["apiKey"] = self.api_key

        response = requests.get(self.base_url + path, params=query_params)
        return response.json()
