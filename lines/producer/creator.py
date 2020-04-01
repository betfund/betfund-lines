"""Kafka Publish Modules."""
import json
import os

from kafka import KafkaProducer


class EventProducer(object):
    """Event Producer Object."""

    def __init__(self):
        self._server = os.getenv("KAFKA_BOOTSTRAP_SERVER")  # temporary
        self._topic = os.getenv("KAFKA_TOPIC")

    def send(self, record: dict):
        """Implements `KafkaProducer.send(...)`."""
        if not isinstance(record, dict):
            raise ValueError

        producer = self._build_producer()

        # TODO: Error handling and logging

        response = producer.send(
            topic=self._topic, value=record
        )

        return response

    def metrics(self):
        """Fetch Metrics of Producer."""
        producer = self._build_producer()

        return producer.metrics()

    def _build_producer(self):
        """Builder of KafkaProducer."""
        producer = KafkaProducer(
            bootstrap_servers=self._server,
            value_serializer=(
                lambda mes: json.dumps(mes).encode("utf-8")
            ),
        )

        return producer
