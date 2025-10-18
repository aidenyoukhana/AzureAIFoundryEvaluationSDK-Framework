import pytest
import json
import os
import allure

# Adjust path if needed
data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "general_purpose"
)

from evaluators.general_purpose.coherence_evaluator import CoherenceEvaluator


@allure.feature("General Purpose Evaluators")
@allure.story("Coherence Evaluation")
@allure.description("Test the CoherenceEvaluator with sample data to ensure it produces valid coherence scores.")
def test_coherence_evaluator():
    evaluator = CoherenceEvaluator()
    data_file = os.path.join(data_dir, "coherence_data.jsonl")
    with open(data_file, "r") as f:
        for line_num, line in enumerate(f, start=1):
            data = json.loads(line.strip())
            with allure.step(f"Evaluating coherence for query {line_num}"):
                allure.attach(json.dumps(data, indent=2), name="Input Data", attachment_type=allure.attachment_type.JSON)
                result = evaluator.evaluate(data["query"], data["response"])
                allure.attach(json.dumps(result, indent=2), name="Evaluation Result", attachment_type=allure.attachment_type.JSON)
                print(json.dumps({"query": data["query"], "response": data["response"], "result": result}, indent=2))
                # Assert based on result structure, e.g., result['coherence'] > 0.5
                assert result is not None
                assert "coherence" in result
                assert isinstance(result["coherence"], (int, float))