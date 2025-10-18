import os
from azure.ai.evaluation import (
    RetrievalEvaluator as AzureRetrievalEvaluator,
    AzureOpenAIModelConfiguration,
)
from dotenv import load_dotenv

load_dotenv()


class RetrievalEvaluator:
    def __init__(self):
        model_config = AzureOpenAIModelConfiguration(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )
        self.evaluator = AzureRetrievalEvaluator(model_config=model_config)

    def evaluate(self, query, retrieved_documents, ground_truth_documents):
        # RetrievalEvaluator expects 'context' parameter which is the retrieved documents as a string
        context = "\n".join(retrieved_documents) if isinstance(retrieved_documents, list) else retrieved_documents
        return self.evaluator(query=query, context=context)
