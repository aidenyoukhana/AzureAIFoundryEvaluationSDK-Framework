import pytest
import json
import os

# Adjust path if needed
data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "general_purpose"
)

from evaluators.general_purpose.qa_evaluator import QAEvaluator


def test_qa_evaluator():
    evaluator = QAEvaluator()
    data_file = os.path.join(data_dir, "qa_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(
                data["query"], data["response"], data.get("context")
            )
            print(json.dumps({"query": data["query"], "response": data["response"], "context": data.get("context"), "result": result}, indent=2))
            assert result is not None