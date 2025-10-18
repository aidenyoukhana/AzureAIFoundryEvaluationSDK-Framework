import os
from azure.ai.evaluation import (
    ToolCallAccuracyEvaluator as AzureToolCallAccuracyEvaluator,
    AzureOpenAIModelConfiguration,
)
from dotenv import load_dotenv

load_dotenv()


class ToolCallAccuracyEvaluator:
    def __init__(self):
        model_config = AzureOpenAIModelConfiguration(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )
        self.evaluator = AzureToolCallAccuracyEvaluator(model_config=model_config)

    def evaluate(self, query, response, tool_calls):
        return self.evaluator(query=query, response=response, tool_calls=tool_calls)
