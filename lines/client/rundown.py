"""Client for TheRundown API."""
import datetime
import os
import requests

from lines.client.config import RundownSportId
from lines.libs import LinesResponseFacade


class RundownClient(object):
    """TheRundown API Wrapper Client."""

    def __init__(self):
        """Constructor for RundownClient."""
        self.base_url = "https://therundown-therundown-v1.p.rapidapi.com/"
        self._api_host = os.getenv("RUNDOWN_API_HOST")
        self._api_key = os.getenv("RUNDOWN_API_KEY")
        self._today = datetime.datetime.now()

    def __repr__(self):
        """Representation for RundownClient."""
        return "<RundownClient: {}>".format(str(self._today))

    def lines(self, sport_id: int):
        """
        Fetch live lines via TheRundown.

        Args:
            sport_id: (int) - SportId for TheRundown API request
        Returns:
            response.json(): (dict) - response object jsonized
            NOTE: raises for invalid SportId and HTTP status
        """
        if sport_id not in RundownSportId._value2member_map_:
            raise ValueError("{} is not a valid SportId".format(sport_id))

        url_extras = "sports/{}/events/{}".format(
            str(sport_id), self._today.strftime("%Y-%m-%d")
        )
        request_url = self.base_url + url_extras

        params = {"include": ["all_periods", "scores"], "offset": "0"}

        headers = {"x-rapidapi-host": self._api_host, "x-rapidapi-key": self._api_key}

        response = requests.get(url=request_url, headers=headers, params=params)
        response.raise_for_status()

        return LinesResponseFacade(response.json())
