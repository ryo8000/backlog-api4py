
import unittest

from backlog import (
    BacklogApi
)


class TestBacklogApi(unittest.TestCase):
    def test_do_something(self):
        backlog_api = BacklogApi()
        self.assertEqual(backlog_api.do_something(), "hello")
