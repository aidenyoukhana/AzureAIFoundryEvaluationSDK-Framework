import pytest
import json
import os
import allure

# Adjust path if needed
data_dir = os.path.join(
    os.path.dirname(__file__), "..", "..", "data", "general_purpose"
)

from evaluators.general_purpose.fluency_evaluator import FluencyEvaluator


@allure.feature("General Purpose Evaluators")
@allure.story("Fluency Evaluation")
@allure.description("Test the FluencyEvaluator with sample data to ensure it produces valid fluency scores.")
def test_fluency_evaluator():
    evaluator = FluencyEvaluator()
    data_file = os.path.join(data_dir, "fluency_data.jsonl")
    with open(data_file, "r") as f:
        for line_num, line in enumerate(f, start=1):
            data = json.loads(line.strip())
            with allure.step(f"Evaluating fluency for query {line_num}"):
                allure.attach(json.dumps(data, indent=2), name="Input Data", attachment_type=allure.attachment_type.JSON)
                result = evaluator.evaluate(data["query"], data["response"])
                allure.attach(json.dumps(result, indent=2), name="Evaluation Result", attachment_type=allure.attachment_type.JSON)
                print(json.dumps({"query": data["query"], "response": data["response"], "result": result}, indent=2))
                assert result is not None
                assert "fluency" in result
                assert isinstance(result["fluency"], (int, float))