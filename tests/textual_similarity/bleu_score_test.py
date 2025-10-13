import pytest
import json
import os

data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "textual_similarity"
)

from evaluators.textual_similarity.bleu_score_evaluator import BleuScoreEvaluator


def test_bleu_score_evaluator():
    evaluator = BleuScoreEvaluator()
    data_file = os.path.join(data_dir, "bleu_score_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["response"], data["ground_truth"])
            print(json.dumps({"response": data["response"], "ground_truth": data["ground_truth"], "result": result}, indent=2))
            assert result is not None