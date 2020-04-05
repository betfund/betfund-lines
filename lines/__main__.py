"""Main Runner for betfind-lines"""
from lines.flow import lines

from prefect.engine.state import State


def runner(sport: int) -> State:
    """
    Main executor for betfind-lines.

    `runner` will execute "betfund-lines-flow"
    There will be individual flow for all RundownSportId

    Args:
        sport (int): Integer of sportId for TheRundown API

    Returns:
        flow_state (State): Final `State` of executed flow
    """
    flow_state = lines(sport)

    return flow_state


if __name__ == "__main__":
    runner(sport=2)  # for testing purposes
