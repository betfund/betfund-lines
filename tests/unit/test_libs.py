"""Unit tests for `lines.libs` modules."""
from unittest import TestCase

from lines.libs.facades import LinesEventFacade, LinesResponseFacade
from tests.utils import load_json


class TestLinesEventFacade(TestCase):
    """Unit tests for `libs.facades.LinesEventFacade`."""

    def setUp(self) -> None:
        """Instantiate LinesEventFacade"""
        self.resp = load_json("testData/nfl-week-three.json")
        self.line_event = self.resp.get("events")[0]
        self.test_facade = LinesEventFacade(self.line_event)

    def test_access(self):
        """Unit test for  facade accesses."""
        assert isinstance(self.test_facade.event_id, str)
        assert isinstance(self.test_facade.sport_id, int)
        assert isinstance(self.test_facade.event_date, str)
        assert isinstance(self.test_facade.score, dict)
        assert isinstance(self.test_facade.teams_normalized, list)
        assert isinstance(self.test_facade.schedule, dict)
        assert isinstance(self.test_facade.line_periods, dict)


class TestLinesResponseFacade(TestCase):
    """Unit tests for `libs.facades.LineResponseFacade`."""

    def setUp(self) -> None:
        """Instantiate LinesResponseFacade"""
        self.resp = load_json("testData/nfl-week-three.json")
        self.test_facade = LinesResponseFacade(self.resp)

    def test_access(self):
        """Unit test for  facade accesses."""
        assert isinstance(self.test_facade.meta, dict)
        assert isinstance(self.test_facade.events, list)
        assert len(self.test_facade.events) == 13
