"""Mock Objects for pytest."""
from tests.utils import load_json


class MockRequestsResponse(object):
    """MockRequestsResponse object."""

    def __init__(self, filepath: str):
        self._path = filepath

    @staticmethod
    def raise_for_status():
        return None

    def json(self):
        return load_json(self._path)
