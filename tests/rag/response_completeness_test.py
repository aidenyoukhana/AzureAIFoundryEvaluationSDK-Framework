import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "rag")

from evaluators.rag.response_completeness_evaluator import ResponseCompletenessEvaluator


def test_response_completeness_evaluator():
    evaluator = ResponseCompletenessEvaluator()
    data_file = os.path.join(data_dir, "response_completeness_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            # ResponseCompletenessEvaluator requires ground_truth parameter
            ground_truth = data.get("ground_truth", data["response"])
            result = evaluator.evaluate(data["query"], data["response"], ground_truth)
            print(json.dumps({"query": data["query"], "response": data["response"], "ground_truth": ground_truth, "result": result}, indent=2))
            assert result is not None