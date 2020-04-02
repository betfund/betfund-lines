"""Client for TheRundown API."""
import datetime
import os
import requests

from prefect import Task

from lines.client.config import RundownSportId
from lines.libs.errors import InvalidSportIdError
from lines.libs.facades import LinesResponseFacade


class Rundown(Task):
    """
    TheRundown API Wrapper Task.

    Rundown is a purely designed API wrapper for TheRundown.io REST API
    The task will be mapped to fetch lines for many sports

    This will be carried out by interval schedule and mapped according.

    Args:
        sport: (int) - sport_id value of `RundownSportId`
    Returns:
        lines: (LinesResponseFacade) - facade of response object `.json()`
    """

    def __init__(self):
        """Constructor for Rundown"""
        self.base_url = "https://therundown-therundown-v1.p.rapidapi.com/"
        self.rundown_host = os.getenv("RUNDOWN_HOST")
        self.rundown_key = os.getenv("RUNDOWN_KEY")
        super().__init__()

    def run(self, sport) -> LinesResponseFacade:
        """Runner for Task."""
        lines = self._fetch(sport=sport)

        return lines

    def _fetch(self, sport) -> LinesResponseFacade:
        """
        Fetch live lines via TheRundown.

        Args:
            sport: (int) - sportId integer for TheRundown request
        Returns:
            lines: (LinesResponseFacade) - facade of response object `.json()`
            NOTE: raises for InvalidSportId and `Response.raise_for_status()`
        """
        if sport not in RundownSportId._value2member_map_:
            raise InvalidSportIdError(
                "Valid `sport` values: {}".format(
                    RundownSportId.list()
                )
            )

        now = datetime.datetime.now()
        url_extras = "sports/{}/events/{}".format(
            str(sport), now.strftime("%Y-%m-%d")
        )

        request_url = self.base_url + url_extras

        params = {
            "include": [
                "all_periods",
                "scores"
            ],
            "offset": "0"
        }

        headers = {
            "x-rapidapi-host": self.rundown_host,
            "x-rapidapi-key": self.rundown_key
        }

        response = requests.get(
            url=request_url, headers=headers, params=params
        )
        response.raise_for_status()

        lines = LinesResponseFacade(
            response.json()
        )

        return lines
