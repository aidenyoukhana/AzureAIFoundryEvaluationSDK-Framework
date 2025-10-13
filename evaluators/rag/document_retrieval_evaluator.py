import os
from azure.ai.evaluation import (
    DocumentRetrievalEvaluator as AzureDocumentRetrievalEvaluator,
    AzureOpenAIModelConfiguration,
)
from dotenv import load_dotenv

load_dotenv()


class DocumentRetrievalEvaluator:
    def __init__(self):
        # DocumentRetrievalEvaluator doesn't require model_config
        # It needs ground_truth_label_min and ground_truth_label_max
        self.evaluator = AzureDocumentRetrievalEvaluator(
            ground_truth_label_min=0,
            ground_truth_label_max=4
        )

    def evaluate(self, query, retrieved_documents, ground_truth_documents):
        # DocumentRetrievalEvaluator expects specific format with document_id and relevance_score
        # Convert our data format to the expected format
        retrieval_ground_truth = [
            {"document_id": str(i), "query_relevance_label": 4 if doc in ground_truth_documents else 2}
            for i, doc in enumerate(retrieved_documents)
        ]
        retrieved_docs = [
            {"document_id": str(i), "relevance_score": 100.0 - i * 10}
            for i in range(len(retrieved_documents))
        ]
        return self.evaluator(retrieval_ground_truth=retrieval_ground_truth, retrieved_documents=retrieved_docs)
