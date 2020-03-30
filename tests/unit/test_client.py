"""Unit tests for `lines.client` modules."""
import datetime
import mock
import pytest
import requests

from unittest import TestCase

from lines.client.rundown import RundownClient
from tests.helpers import MockRequestsResponse


class TestRundownClient(TestCase):
    """Unit tests for RundownClient."""

    @mock.patch("lines.client.rundown.datetime")
    def setUp(self, mock_datetime) -> None:
        """Instantiate RundownClient"""
        mock_datetime.return_value = mock.Mock(
            return_value=datetime.datetime(2020, 3, 1, 0, 0)
        )
        self.test_client = RundownClient()
        self.test_client._api_host = "some-host"
        self.test_client._api_key = "you-will-never-guess"
        self.test_client._today = mock_datetime.return_value

    def test_constructor(self):
        """Unit test for `RundownClient.__init__(...)` success."""
        assert self.test_client._api_host == "some-host"
        assert self.test_client._api_key == "you-will-never-guess"

    def test_repr(self):
        """Unit test for `RundownClient.__repr(...)` success."""
        assert self.test_client.__repr__().startswith("<RundownClient")

    @mock.patch.object(requests, "get")
    def test_lines(self, mock_rundown_resp):
        """Unit test for `RundownClient.lines(...)` success."""
        mock_rundown_resp.return_value = MockRequestsResponse(
            filepath="testData/nfl-week-three.json"
        )

        response = self.test_client.lines(sport_id=2)

        assert isinstance(response, dict)
        assert isinstance(response.events, list)
        assert isinstance(response.meta, dict)
        assert len(response.events) == 13

    def test_lines_raises(self):
        """Unit test for `RundownClient.lines(...)` raises."""
        with pytest.raises(ValueError):
            self.test_client.lines(sport_id=12093)
