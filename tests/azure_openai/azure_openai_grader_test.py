import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "azure_openai")

from evaluators.azure_openai.azure_openai_grader import AzureOpenAIGrader


def test_azure_openai_grader():
    grader = AzureOpenAIGrader()
    data_file = os.path.join(data_dir, "grader_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            # Pass the full data dictionary to the grader
            result = grader.evaluate(data)
            print(json.dumps({"data": data, "result": result}, indent=2))
            assert result is not None