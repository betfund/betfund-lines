"""Temporal Data store Response Objects."""
from abc import abstractmethod


class TemporalClientResponse(object):
    """Temporal Response Objects."""

    @abstractmethod
    def __call__(self):
        raise NotImplementedError("this-should-be-implemented")


class TemporalClientSuccess(TemporalClientResponse):
    """Success Response."""

    def __call__(self):
        return {"status": 200, "message": "SUCCESS"}


class TemporalClientFailure(TemporalClientResponse):
    """Error Response."""

    def __call__(self):
        return {"status": 418, "message": "IM A TEAPOT!"}
