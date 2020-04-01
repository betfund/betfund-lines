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


if __name__ == '__main__':
    from itertools import chain
    myd = load_json("testData/output.json")

    props = myd.get("properties")
    data = props.get("data").get("properties")
    line_periods = data.get("linePeriods")
    lpp = line_periods.get("properties")

    prev = None
    for k, v in lpp.items():
        pps = v.get("properties")
        if prev:
            print(set(pps) == prev)
        prev = set(pps)
        print(f"{k}: Props: {len(pps)}")
    import pdb; pdb.set_trace()

#     all_of_em = []
#     def recursive_items(dictionary):
#         for key, value in dictionary.items():
#             all_of_em.append(key)
#             if type(value) is dict:
#                 yield from recursive_items(value)
#             else:
#                 yield (key, value)
#
#
#     for key, value in recursive_items(myd):
#         all_of_em.append(key)
#
# import pdb; pdb.set_trace()