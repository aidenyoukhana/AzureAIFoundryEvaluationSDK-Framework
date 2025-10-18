import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "risk_safety")

from evaluators.risk_safety.violence_evaluator import ViolenceEvaluator


def test_violence_evaluator():
    evaluator = ViolenceEvaluator()
    data_file = os.path.join(data_dir, "violence_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["query"], data["response"])
            print(json.dumps({"query": data["query"], "response": data["response"], "result": result}, indent=2))
            assert result is not None