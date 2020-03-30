"""Runner for BetFund Temporal Datastore."""
import sys

from lines.client import RundownClient
from lines.snapshot import TemporalToSnapshot
from lines.temporal import BetFundTemporalClient


def run(sport_id: int):  # pragma: no cover
    DEBUG = False  # DO NOT CHECK IN AS TRUE
    if DEBUG is True:
        sys.exit()

    rdc = RundownClient()
    lines = rdc.lines(sport_id=sport_id)

    if not lines.events:
        return None

    ssc = TemporalToSnapshot()
    tdsc = BetFundTemporalClient()

    for line in lines.events:  # multiprocess here (later)
        ss = ssc.generate(line)
        tdsc.put_temporal(ss)


if __name__ == "__main__":
    run(sport_id=2)  # Client side call to lines by sport
