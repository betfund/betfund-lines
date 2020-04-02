"""Unit tests for `lines.transformer` modules."""
import pytest

from unittest import TestCase

from lines.libs.errors import MalformedKeyError
from lines.libs.facades import LinesEventFacade
from lines.transformer.transform import RundownTransformer


from tests.utils import load_json


class TestRundownTransformer(TestCase):
    """Unit tests for `libs.snapshot.RundownTransformer`."""

    def setUp(self) -> None:
        """Instantiate TemporalToSnapshot"""
        self.resp = load_json("testData/nfl-week-three.json")
        self.line_event = LinesEventFacade(self.resp.get("events")[0])
        self.test_transformer = RundownTransformer()

    def test_constructor(self):
        """Unit test for `RundownTransformer.__init__(...)` success."""
        assert self.test_transformer.log_level == "INFO"

    def test_generate(self):
        """Unit test for `RundownTransformer._generate(...)` success."""
        result = self.test_transformer._generate(
            record=self.line_event
        )

        assert isinstance(result, dict)

    def test_generate_raises(self):
        """Unit test for `RundownTransformer._generate(...)` raises."""
        with pytest.raises(MalformedKeyError):
            self.test_transformer._generate(
                record=LinesEventFacade({})
            )