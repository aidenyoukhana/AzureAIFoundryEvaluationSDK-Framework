import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "agentic")

from evaluators.agentic.task_adherence_evaluator import TaskAdherenceEvaluator


def test_task_adherence_evaluator():
    evaluator = TaskAdherenceEvaluator()
    data_file = os.path.join(data_dir, "task_adherence_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(data["query"], data["response"], data["task"])
            print(json.dumps({
                "query": data['query'],
                "response": data['response'],
                "task": data['task'],
                "result": result
            }, indent=2))
            assert result is not None