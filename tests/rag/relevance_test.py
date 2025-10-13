import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "rag")

from evaluators.rag.relevance_evaluator import RelevanceEvaluator


def test_relevance_evaluator():
    evaluator = RelevanceEvaluator()
    data_file = os.path.join(data_dir, "relevance_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(
                data["query"], data["response"], data["context"]
            )
            print(json.dumps({"query": data["query"], "response": data["response"], "context": data["context"], "result": result}, indent=2))
            assert result is not None