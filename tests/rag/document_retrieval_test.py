import pytest
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "rag")

from evaluators.rag.document_retrieval_evaluator import DocumentRetrievalEvaluator


def test_document_retrieval_evaluator():
    evaluator = DocumentRetrievalEvaluator()
    data_file = os.path.join(data_dir, "document_retrieval_data.jsonl")
    with open(data_file, "r") as f:
        for line in f:
            data = json.loads(line.strip())
            result = evaluator.evaluate(
                data["query"],
                data["retrieved_documents"],
                data["ground_truth_documents"],
            )
            print(json.dumps({"query": data["query"], "retrieved_documents": data["retrieved_documents"], "ground_truth_documents": data["ground_truth_documents"], "result": result}, indent=2))
            assert result is not None