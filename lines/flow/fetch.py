"""Prefect Flow Builder."""
import os

from datetime import timedelta

from prefect import Flow, Parameter
from prefect.engine.state import State
from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock

from lines.client.rundown import Rundown
from lines.producer.sender import EventProducer
from lines.transformer.transform import RundownTransformer


def build(sport: int) -> Flow:
    """
    Build flow via imperative API.

    `schedule` - is an IntervalClock Prefect schedule
    This is defined by an arbitrary timedelta

    Args:
        sport (int): sportId for TheRundownAPI request.

    Returns:
        flow (Flow): Prefect `Flow` constructed
        `flow` consists of 3 subclasses of `Task`
            Rundown(Task)
            RundownTransformer(Task)
            KafkaProducer(Task)
    """
    schedule = Schedule(
        clocks=[
            IntervalClock(interval=timedelta(
                hours=os.getenv("PREFECT_INTERVAL"))
            )
        ]
    )

    rundown_client = Rundown()
    rundown_transformer = RundownTransformer()
    kafka_producer = EventProducer()

    with Flow("betfund-lines-flow") as flow:
        sport = Parameter("sport")

        # Using Prefect's Imperative API
        # Dependencies are set with `keyword_tasks`
        # A `keyword_task` is a result of a task...
        # ...that is a dependency of the `task`

        flow.schedule = schedule
        flow.set_dependencies(
            task=rundown_client,
            keyword_tasks=(dict(sport=sport))
        )
        flow.set_dependencies(
            task=rundown_transformer,
            mapped=True,
            keyword_tasks=dict(record=rundown_client),
            upstream_tasks=[rundown_client],
        )
        flow.set_dependencies(
            task=kafka_producer,
            mapped=True,
            keyword_tasks=dict(record=rundown_transformer),
            upstream_tasks=[rundown_transformer],
        )

    return flow


def execute(flow: Flow, sport: int) -> State:
    """
    Execute `betfund-lines` flow build in `_build(...)`.

    Args:
        flow (Flow): Prefect `Flow` constructed by `build(...)`
        sport (int): sportId for TheRundownAPI request.

    Returns:
        flow_state (State): state of completed Prefect `Flow`
    """
    flow_state = flow.run(
        sport=sport, run_on_schedule=True
    )

    return flow_state


def lines(sport: int) -> State:
    """
    Caller for `betfund-lines` flow.

    Args:
        sport (int): TheRundown `sportId` for API request
    Returns:
        lines_state (state): state of `betfund-lines` flow
    """
    flow = build(sport=sport)
    lines_state = execute(flow=flow, sport=sport)

    return lines_state.serialize()
