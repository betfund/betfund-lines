"""Runner for `betfund-lines`."""
import sys

from lines.client import RundownClient
from lines.transformer import RundownTransformer


def run(sport_id: int):
    DEBUG = False  # DO NOT CHECK IN AS TRUE
    if DEBUG is True:
        sys.exit()

    # rdc = RundownClient()
    # lines = rdc.lines(sport_id=sport_id)
    #
    # if not lines.events:
    #     return None
    from lines.libs.facades import LinesResponseFacade
    import json
    with open("tests/testData/teste.json", "r") as d:
        lines = LinesResponseFacade(json.loads(d.read()))


    ssc = RundownTransformer()
    for line in lines.events:

        data = ssc.generate(line)
        print(data)
        break

    return ssc

if __name__ == '__main__':
    run(sport_id=2)