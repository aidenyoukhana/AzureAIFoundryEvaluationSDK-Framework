import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "agentic")

from evaluators.agentic.intent_resolution_evaluator import IntentResolutionEvaluator


def test_intent_resolution_evaluator():
    evaluator = IntentResolutionEvaluator()
    data_file = os.path.join(data_dir, "intent_resolution_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["query"], data["response"], data["intent"])
            print(json.dumps({
                "query": data['query'],
                "response": data['response'],
                "intent": data['intent'],
                "result": result
            }, indent=2))
            assert result is not None