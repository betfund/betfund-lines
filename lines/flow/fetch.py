"""Flow builder."""
from prefect import Flow, Parameter
from prefect.engine.state import State

from lines.client.rundown import Rundown
from lines.producer.sender import KafkaProducer
from lines.transformer.transform import RundownTransformer


def build(sport: int) -> Flow:
    """
    Build flow via imperative API.

    Args:
        sport (int): sportId for TheRundownAPI request.

    Returns:
        flow (Flow): Prefect `Flow` constructed
        `flow` consists of 3 subclasses of `Task`
            Rundown(Task)
            RundownTransformer(Task)
            KafkaProducer(Task)
    """
    rundown_client = Rundown()
    rundown_transformer = RundownTransformer()
    kafka_proucer = KafkaProducer()

    with Flow("betfund-lines") as flow:
        sport = Parameter("sport")

        # Using Prefect's Imperative API
        # Dependencies are set with `keyword_tasks`
        # A `keyword_task` is a result of a task...
        # ...that is a dependency of the `task`

        flow.set_dependencies(
            task=rundown_client, keyword_tasks=(dict(sport=sport))
        )
        flow.set_dependencies(
            task=rundown_transformer,
            mapped=True,
            keyword_tasks=dict(record=(rundown_client))
        )
        flow.set_dependencies(
            task=kafka_proucer,
            mapped=True,
            keyword_tasks=dict(record=(rundown_transformer))
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
        sport=sport
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
    lines_state = execute(
        flow=flow, sport=sport
    )

    return lines_state.serialize()
