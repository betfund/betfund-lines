"""Temporal Storage Client."""
import json
import logging
import os

from lines.temporal.response import (
    TemporalClientFailure,
    TemporalClientSuccess,
)

logging.basicConfig(level="INFO")
_LOGGER = logging.getLogger(__name__)


class BetFundTemporalClient(object):  # pragma: no cover
    """BetFundTemporalClient object."""

    def __init__(self):
        """Constructor for BetFundTemporalClient."""
        self.loc = os.path.expanduser("betfund/temporal/testDatastore/test.json")
        self.db = self.load()

    def load(self) -> dict:
        """Load database into memory."""
        if os.path.exists(self.loc):
            loaded = self._load()
        else:
            loaded = {}

        return loaded

    def dump(self):
        """Dump to self.db."""
        try:
            json.dump(self.db, open(self.loc, "w+"))
            return True

        except Exception:
            return False

    def put_temporal(self, record: dict):
        """`PUT` operation into `betfund.db`."""
        if not (record.get("key"), record.get("data")):
            raise ValueError(
                "Malformed Payload: {}".format(json.dumps(record, indent=4))
            )

        if self._exist(key=record.get("key")):
            try:
                self.db.get(record.get("key").get("eventId")).append(record)

                _LOGGER.info(
                    "PUT: UPDATE - eventId: {}".format(record["key"].get("eventId"))
                )

                self.dump()

            except Exception:
                _LOGGER.error(
                    "PUT: FAILURE - eventId: {}".format(record["key"].get("eventId"))
                )
                return TemporalClientFailure()

            return TemporalClientSuccess()

        try:
            self.db[record.get("key").get("eventId")] = [record]
            _LOGGER.info("PUT: NEW - eventId: {}".format(record["key"].get("eventId")))

            self.dump()

        except Exception:
            _LOGGER.error(
                "PUT: FAILURE - eventId: {}".format(record["key"].get("eve`ntId"))
            )
            return TemporalClientFailure()

        return TemporalClientSuccess()

    def _load(self) -> dict:
        """Helper for `self.load(...)`"""
        self.db = json.load(open(self.loc, "r"))
        return self.db

    def _exist(self, key: dict) -> bool:
        """
        Check for existence of key in data store.

        Args:
            key: (dict) - search index for database
            (e.g.)
                {
                    "eventId": "129slaskdfj10801ls",
                    "sportId": 2
                }
        Returns:
            _exists: (bool) - boolean for key existence
        """
        if not isinstance(key, dict):
            raise ValueError(
                "The provided key is invalid: {}".format(json.dumps(key, indent=4))
            )

        return bool(self.db.get(key.get("eventId")))
