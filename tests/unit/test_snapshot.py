"""Unit tests for `lines.snapshot` modules."""
import pytest

from unittest import TestCase

from lines.libs import LinesEventFacade
from lines.snapshot import TemporalToSnapshot
from tests.utils import load_json


class TestTemporalToSnapshot(TestCase):
    """Unit tests for `libs.snapshot.TemporalToSnapshot`."""

    def setUp(self) -> None:
        """Instantiate TemporalToSnapshot"""
        self.resp = load_json("testData/nfl-week-three.json")
        self.line_event = LinesEventFacade(self.resp.get("events")[0])
        self.test_ttss = TemporalToSnapshot()

    def test_constructor(self):
        """Unit test for `TemporalToSnapshot.__init__(...)` success."""
        assert self.test_ttss.log_level == "info"

    def test_generate(self):
        """Unit test for `TemporalToSnapshot.generate(...)` success."""
        result = self.test_ttss.generate(
            record=self.line_event
        )

        assert isinstance(result, dict)

    def test_generate_raises(self):
        """Unit test for `TemporalToSnapshot.generate(...)` raises."""
        with pytest.raises(ValueError):
            self.test_ttss.generate(
                record=LinesEventFacade({})
            )