import pytest
import json
import os

# Adjust path if needed
data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "general_purpose"
)

from evaluators.general_purpose.coherence_evaluator import CoherenceEvaluator


def test_coherence_evaluator():
    evaluator = CoherenceEvaluator()
    data_file = os.path.join(data_dir, "coherence_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["query"], data["response"])
            print(json.dumps({"query": data["query"], "response": data["response"], "result": result}, indent=2))
            # Assert based on result structure, e.g., result['coherence_score'] > 0.5
            assert result is not None