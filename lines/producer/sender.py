"""Kafka Publish Modules."""
import json
import os

from kafka import KafkaProducer
from prefect import Task

from lines.libs.errors import MalformedPayloadError


class EventProducer(Task):
    """
    Event Producer Object.

    EventProducer handles produces events via `.send(...)` in a Kafka topic

    Args:
        record (dict): Record produced by `RundownTransformer`

    Returns:
        response (FutureRecordMetadata): resolves to RecordMetadata
    """

    def __init__(self):
        self.server = os.getenv("KAFKA_BOOTSTRAP_SERVER")  # temporary
        self.topic = os.getenv("KAFKA_TOPIC")
        super().__init__()

    def run(self, record: dict):
        """
        Implements `KafkaProducer.send(...)`.

        Args:
            record (dict): Record produced by `RundownTransformer`

        Returns:
            response (FutureRecordMetadata): resolves to RecordMetadata

        Raises:
            MalformedPayloadError: if `record` is not literal `dict`
        """
        if not isinstance(record, dict):
            raise MalformedPayloadError(
                "Invalid Payload: {}".format(
                    json.dumps(record, indent=4)
                )
            )

        producer = self._build_producer()

        response = producer.send(
            topic=self.topic, value=record
        )

        return response

    def _build_producer(self):
        """
        Build KafkaProducer Client.

        Returns:
            producer (KafkaProducer): Kafka Producer for self.server
        """
        producer = KafkaProducer(
            bootstrap_servers=self.server,
            value_serializer=(
                lambda mes: json.dumps(mes).encode("utf-8")
            ),
        )

        return producer
