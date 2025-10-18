import os
from azure.ai.evaluation import (
    CoherenceEvaluator as AzureCoherenceEvaluator,
    AzureOpenAIModelConfiguration,
)
from dotenv import load_dotenv

load_dotenv()


class CoherenceEvaluator:
    def __init__(self):
        model_config = AzureOpenAIModelConfiguration(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )
        self.evaluator = AzureCoherenceEvaluator(model_config=model_config)

    def evaluate(self, query, response):
        return self.evaluator(query=query, response=response)
