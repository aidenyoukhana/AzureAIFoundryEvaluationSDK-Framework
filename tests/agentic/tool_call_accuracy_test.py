import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "agentic")

from evaluators.agentic.tool_call_accuracy_evaluator import ToolCallAccuracyEvaluator


def test_tool_call_accuracy_evaluator():
    evaluator = ToolCallAccuracyEvaluator()
    data_file = os.path.join(data_dir, "tool_call_accuracy_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(
                data["query"], data["response"], data["tool_calls"]
            )
            print(json.dumps({
                "query": data['query'],
                "response": data['response'],
                "tool_calls": data['tool_calls'],
                "result": result
            }, indent=2))
            assert result is not None