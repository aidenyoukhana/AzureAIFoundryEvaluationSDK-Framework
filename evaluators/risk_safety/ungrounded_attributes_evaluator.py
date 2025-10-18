import os
from azure.ai.evaluation import (
    UngroundedAttributesEvaluator as AzureUngroundedAttributesEvaluator,
)
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()


class UngroundedAttributesEvaluator:
    def __init__(self):
        credential = DefaultAzureCredential()
        azure_ai_project = {
            "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
            "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP"),
            "project_name": os.environ.get("AZURE_PROJECT_NAME"),
        }
        self.evaluator = AzureUngroundedAttributesEvaluator(
            azure_ai_project=azure_ai_project, credential=credential
        )

    def evaluate(self, query, response, context=None):
        # UngroundedAttributesEvaluator requires context parameter
        if context is None:
            # Provide a minimal context if not given
            context = "No specific context provided."
        return self.evaluator(query=query, response=response, context=context)
