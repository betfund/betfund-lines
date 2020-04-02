"""Flow builder."""
import os  # noqa: F403, F401
from datetime import timedelta  # noqa: F403, F401

from prefect import Flow, Parameter
from prefect.engine.executors import DaskExecutor  # noqa: F403, F401
from prefect.engine.state import State
from prefect.schedules import IntervalSchedule  # noqa: F403, F401
from prefect.utilities.debug import raise_on_exception  # noqa: F403, F401

from lines.client.rundown import Rundown
from lines.transformer.transform import RundownTransformer


def build(sport: int) -> Flow:
    """Build flow via imperative API."""
    rdc = Rundown()
    rtc = RundownTransformer()

    with Flow("betfund-lines") as flow:
        sport = Parameter("sport")

        lines = rdc(sport)

        rtc.map(
            record=lines
        )

    return flow


def execute(flow: Flow, sport: int) -> State:
    """Execute `betfund-lines` flow build in `_build(...)`."""
    records = flow.run(
        sport=sport
    )

    return records


def lines(sport: int) -> State:
    """
    Caller for `betfund-lines` flow.

    Args:
        sport: (int) - TheRundown `sportId`
    Returns:
        lines_state: (state) state of `betfund-lines` flow
    """
    flow = build(sport=sport)
    lines_state = execute(
        flow=flow, sport=sport
    )

    return lines_state.serialize()
