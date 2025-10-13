import pytest
import json
import os

# Adjust path if needed
data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "general_purpose"
)

from evaluators.general_purpose.fluency_evaluator import FluencyEvaluator


def test_fluency_evaluator():
    evaluator = FluencyEvaluator()
    data_file = os.path.join(data_dir, "fluency_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["query"], data["response"])
            print(json.dumps({"query": data["query"], "response": data["response"], "result": result}, indent=2))
            assert result is not None