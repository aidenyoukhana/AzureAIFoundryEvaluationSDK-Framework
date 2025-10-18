import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "risk_safety")

from evaluators.risk_safety.self_harm_evaluator import SelfHarmEvaluator


def test_self_harm_evaluator():
    evaluator = SelfHarmEvaluator()
    data_file = os.path.join(data_dir, "self_harm_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["query"], data["response"])
            print(json.dumps({"query": data["query"], "response": data["response"], "result": result}, indent=2))
            assert result is not None