import pytest
import json
import os
from evaluators.general_purpose.qa_evaluator import QAEvaluator

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "general_purpose")

def test_qa_evaluator():
    evaluator = QAEvaluator()
    data_file = os.path.join(data_dir, "qa_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(
                query=data["input"],
                response=data["response"],
                context=data["context"],
                ground_truth=data["ground_truth"]
            )
            print(json.dumps({
                "input": data["input"],
                "response": data["response"],
                "context": data["context"],
                "ground_truth": data["ground_truth"],
                "result": result
            }, indent=2))
            assert result is not None
