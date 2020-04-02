"""
Rundown API response transformer mechanism for creating temporal updates.

Generator of temporal records for `lines.producer.creator`

(e.g.)
    Temporal records represented by key: value pairs
    NOTE: this must contain an temporal element
    in this case the field: "event_date" from API response

    "timestamp": "2020-02-02T23:30:00Z" is referenced as temporal element

    {
        "key": {
            "eventId": "9a35b8986a76ea364be331cb453ec",  # string
            "sportId": 2  # integer
        },
        "data": {
            "timestamp": "2020-02-01T17:22:12Z",
            "eventDate": "2020-02-02T23:30:00Z",
            ...
        }
    }
"""
import datetime
import json
from typing import Union

from prefect import Task

from lines.libs.facades import LinesEventFacade
from lines.libs.errors import MalformedKeyError


class RundownTransformer(Task):
    """RundownTransformer object."""

    def __init__(self):
        """Constructor for RundownTransformer."""
        self.log_level = "INFO"
        super().__init__()

    def run(self, record):
        lines = self._generate(record=record)

        return lines

    @staticmethod
    def _generate(record: LinesEventFacade) -> Union[dict, None]:
        """
        Generate temporal record for data store.

        Args:
            record: (LinesEventFacade) - input to generate temporal record for
        Returns:
            transformed: (dict) - schema conforming record
            NOTE: raises ValueError for malformed `key`
        """
        transformed = {
            "key": {
                "eventId": record.event_id,
                "sportId": record.sport_id
            },
            "data": {
                "eventDate": record.event_date,
                "timestamp": str(datetime.datetime.now()),  # temporal element
                "score": record.score,
                "teams": record.teams_normalized,
                "schedule": record.schedule,
                "linePeriods": record.line_periods,
            }
        }

        if not all([record.event_id, record.sport_id]):
            raise MalformedKeyError(
                "Invalid Key: {}".format(
                    json.dumps(transformed.get("key"), indent=4)
                )
            )

        return transformed
