import pytest
import json
import os

data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "textual_similarity"
)

from evaluators.textual_similarity.rouge_score_evaluator import RougeScoreEvaluator


def test_rouge_score_evaluator():
    evaluator = RougeScoreEvaluator()
    data_file = os.path.join(data_dir, "rouge_score_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["response"], data["ground_truth"])
            print(json.dumps({"response": data["response"], "ground_truth": data["ground_truth"], "result": result}, indent=2))
            assert result is not None