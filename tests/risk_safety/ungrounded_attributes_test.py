import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "risk_safety")

from evaluators.risk_safety.ungrounded_attributes_evaluator import UngroundedAttributesEvaluator


def test_ungrounded_attributes_evaluator():
    evaluator = UngroundedAttributesEvaluator()
    data_file = os.path.join(data_dir, "ungrounded_attributes_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            context = data.get("context", None)
            result = evaluator.evaluate(data["query"], data["response"])
            print(json.dumps({"query": data["query"], "response": data["response"], "result": result}, indent=2))
            assert result is not None