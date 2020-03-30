"""Rundown API Response Facades."""
from typing import Union


class LinesResponseFacade(dict):
    """TheRundown `GET events` response accessor."""

    def __init__(self, data: dict):
        super(LinesResponseFacade, self).__init__(data)

    @property
    def meta(self) -> dict:
        """Fetch `meta` key from LineResponse."""
        return self.get("meta")

    @property
    def events(self) -> Union[list, None]:
        """Fetch `events` key from LineResponse."""
        raw_events = self.get("events")
        if not raw_events:
            return None

        events = []
        for event in raw_events:
            events.append(LinesEventFacade(event))

        return events


class LinesEventFacade(dict):
    """TheRundown `GET events.line` response accessor."""

    def __init__(self, event: dict):
        super(LinesEventFacade, self).__init__(event)

    @property
    def event_id(self) -> str:
        """Fetch `event_id` from LineEvent."""
        return self.get("event_id")

    @property
    def sport_id(self) -> int:
        """Fetch `sport_id` from LineEvent."""
        return self.get("sport_id")

    @property
    def event_date(self) -> str:
        """Fetch `event_date` from LineEvent."""
        return self.get("event_date")

    @property
    def score(self) -> dict:
        """Fetch `score` from LineEvent."""
        return self.get("score")

    @property
    def teams_normalized(self) -> list:
        """Fetch `teams_normalized` from LineEvent."""
        return self.get("teams_normalized")

    @property
    def schedule(self) -> dict:
        """Fetch `schedule` from LineEvent."""
        return self.get("schedule")

    @property
    def line_periods(self) -> dict:
        """Fetch `line_periods` from LineEvent."""
        return self.get("line_periods")
