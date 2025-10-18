import os
from azure.ai.evaluation import (
    ResponseCompletenessEvaluator as AzureResponseCompletenessEvaluator,
    AzureOpenAIModelConfiguration,
)
from dotenv import load_dotenv

load_dotenv()


class ResponseCompletenessEvaluator:
    def __init__(self):
        model_config = AzureOpenAIModelConfiguration(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )
        self.evaluator = AzureResponseCompletenessEvaluator(model_config=model_config)

    def evaluate(self, query, response, ground_truth=None):
        # ResponseCompletenessEvaluator requires ground_truth parameter
        # If not provided, use the response itself as a fallback
        if ground_truth is None:
            ground_truth = response
        return self.evaluator(response=response, ground_truth=ground_truth)
