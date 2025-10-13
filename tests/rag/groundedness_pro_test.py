import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "rag")

from evaluators.rag.groundedness_pro_evaluator import GroundednessProEvaluator


def test_groundedness_pro_evaluator():
    evaluator = GroundednessProEvaluator()
    data_file = os.path.join(data_dir, "groundedness_pro_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["response"], data["context"])
            print(json.dumps({"response": data["response"], "context": data["context"], "result": result}, indent=2))
            assert result is not None