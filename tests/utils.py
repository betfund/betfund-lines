"""Test utility modules."""
import json
import os


def load_json(filepath: str) -> dict:
    """Load `json` test file."""
    abs_path = _resolve_relative(filepath)
    with open(abs_path) as f:
        raw_json = f.read()

        return json.loads(raw_json)


def _resolve_relative(filepath: str) -> str:
    """Resolve relative import path."""
    inf_path = os.path.join(os.path.dirname(__file__), filepath)

    return inf_path
