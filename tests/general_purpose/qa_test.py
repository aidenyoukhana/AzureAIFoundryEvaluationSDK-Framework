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
                data["question"], data["answer"], data.get("context"), data["ground_truth"]
            )
            print(json.dumps({"question": data["question"], "answer": data["answer"], "context": data.get("context"), "result": result}, indent=2))
            assert result is not None