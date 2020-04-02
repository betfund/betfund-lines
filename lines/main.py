"""Runner for `betfund-lines`."""
import sys

from lines.client import Rundown  # noqa: F403, F401
from lines.transformer import RundownTransformer  # noqa: F403, F401


def run(sport_id: int):
    DEBUG = False  # DO NOT CHECK IN AS TRUE
    if DEBUG is True:
        sys.exit()
