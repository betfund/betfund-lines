"""Unit tests for `lines.client` modules."""
import mock
import pytest
import requests

from unittest import TestCase

from lines.client.rundown import Rundown
from lines.libs.errors import InvalidSportIdError

from tests.helpers import MockRequestsResponse


class TestRundown(TestCase):
    """Unit tests for Rundown Client."""

    def setUp(self) -> None:
        """Instantiate Rundown."""
        self.test_client = Rundown()
        self.test_client.rundown_host = "some-host"
        self.test_client.rundown_key = "you-will-never-guess"

    def test_constructor(self):
        """Unit test for `Rundown.__init__(...)` success."""
        assert self.test_client.rundown_host == "some-host"
        assert self.test_client.rundown_key == "you-will-never-guess"

    @mock.patch.object(requests, "get")
    def test_run(self, mock_rundown_resp):
        """Unit test for `Rundown._run(...)` success."""
        mock_rundown_resp.return_value = MockRequestsResponse(
            filepath="testData/nfl-week-three.json"
        )

        response = self.test_client.run(sport=2)

        assert isinstance(response, list)
        assert len(response) == 13

    def test_run_raises(self):
        """Unit test for `Rundown._run(...)` raises."""
        with pytest.raises(InvalidSportIdError):
            self.test_client.run(sport=12093)
