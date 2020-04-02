"""Unit tests for `lines.client` modules."""
import datetime
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
    def test_fetch(self, mock_rundown_resp):
        """Unit test for `Rundown._fetch(...)` success."""
        mock_rundown_resp.return_value = MockRequestsResponse(
            filepath="testData/nfl-week-three.json"
        )

        response = self.test_client._fetch(sport=2)

        assert isinstance(response, dict)
        assert isinstance(response.events, list)
        assert isinstance(response.meta, dict)
        assert len(response.events) == 13

    def test_fetch_raises(self):
        """Unit test for `Rundown._fetch(...)` raises."""
        with pytest.raises(InvalidSportIdError):
            self.test_client._fetch(sport=12093)
