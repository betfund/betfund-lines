"""Kafka Publish Modules."""
import json
import os

from kafka import KafkaProducer
from prefect import Task

from lines.libs.errors import MalformedPayloadError


class EventProducer(Task):
    """Event Producer Object."""

    def __init__(self, *args, **kwargs):
        self._server = os.getenv("KAFKA_BOOTSTRAP_SERVER")  # temporary
        self._topic = os.getenv("KAFKA_TOPIC")
        super().__init__(*args, **kwargs)

    def run(self, record: dict):
        """Implements `KafkaProducer.send(...)`."""
        if not isinstance(record, dict):
            raise MalformedPayloadError(
                "Invalid Payload: {}".format(
                    json.dumps(record, indent=4)
                )
            )

        producer = self._build_producer()

        response = producer.send(
            topic=self._topic, value=record
        )

        return response

    def _build_producer(self):
        """Builder of KafkaProducer."""
        producer = KafkaProducer(
            bootstrap_servers=self._server,
            value_serializer=(
                lambda mes: json.dumps(mes).encode("utf-8")
            ),
        )

        return producer
