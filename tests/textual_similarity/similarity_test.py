import pytest
import json
import os

data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "textual_similarity"
)

from evaluators.textual_similarity.similarity_evaluator import SimilarityEvaluator


def test_similarity_evaluator():
    evaluator = SimilarityEvaluator()
    data_file = os.path.join(data_dir, "similarity_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(
                data["query"], data["response"], data["ground_truth"]
            )
            print(json.dumps({"query": data["query"], "response": data["response"], "ground_truth": data["ground_truth"], "result": result}, indent=2))
            assert result is not None