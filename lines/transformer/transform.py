"""
Rundown API response transformer mechanism for creating temporal updates.

Generator of temporal records for `lines.producer.creator`

(e.g.)
    Temporal records represented by key: value pairs
    NOTE: this must contain an temporal element
    in this case the field: "event_date" from API response

    "event_date": "2020-02-02T23:30:00Z" is referenced as temporal element

    {
        "key": {
            "eventId": "9a35b8986a76ea364be331cb453ec",  # string
            "sportId": 2  # integer
        },
        "data": {
            "eventDate": "2020-02-02T23:30:00Z"",
            ...
        }
    }
"""
import json
from lines.libs.facades import LinesEventFacade

from typing import Union


class RundownTransformer(object):
    """RundownTransformer object."""

    def __init__(self):
        """Constructor for RundownTransformer."""
        self.log_level = "INFO"

    def generate(self, record: LinesEventFacade) -> Union[dict, None]:
        """
        Generate temporal record for data store.

        Args:
            record: (LinesEventFacade) - input to generate temporal record for
        Returns:
            temporal_record: (dict) - schema conforming record
            NOTE: raises ValueError for malformed `key`
        """
        temporal_record = {
            "key": {
                "eventId": record.event_id,
                "sportId": record.sport_id
            },
            "data": {
                "eventDate": record.event_date,  # temporal element
                "score": record.score,
                "teams": record.teams_normalized,
                "schedule": record.schedule,
                "linePeriods": record.line_periods,
            }
        }

        if not all([record.event_id, record.sport_id]):
            raise ValueError(
                "Malformed Key: {}".format(
                    json.dumps(temporal_record.get("key"), indent=4)
                )
            )

        return temporal_record
