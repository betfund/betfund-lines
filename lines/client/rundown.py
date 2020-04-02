"""Client for TheRundown API."""
import datetime
import logging
import os
import requests

from prefect import Task

from lines.client.config import RundownSportId
from lines.libs.errors import InvalidSportIdError
from lines.libs.facades import LinesResponseFacade

logging.basicConfig(level="INFO")
_LOGGER = logging.getLogger(__name__)


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

    def __init__(self, *args, **kwargs):
        """Constructor for Rundown"""
        self.base_url = "https://therundown-therundown-v1.p.rapidapi.com"
        self.rundown_host = os.getenv("RUNDOWN_HOST")
        self.rundown_key = os.getenv("RUNDOWN_KEY")
        super().__init__(*args, **kwargs)

    def run(self, sport: int) -> LinesResponseFacade:
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
        request_url = "{}/sports/{}/events/{}".format(
            self.base_url, str(sport), now.strftime("%Y-%m-%d")
        )

        _LOGGER.info(
            "<URL BUILT> {}".format(
                request_url
            )
        )

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

        return lines.events
