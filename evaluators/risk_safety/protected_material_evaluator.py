import os
from azure.ai.evaluation import (
    ProtectedMaterialEvaluator as AzureProtectedMaterialEvaluator,
)
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()


class ProtectedMaterialEvaluator:
    def __init__(self):
        credential = DefaultAzureCredential()
        azure_ai_project = {
            "subscription_id": os.environ.get("AZURE_SUBSCRIPTION_ID"),
            "resource_group_name": os.environ.get("AZURE_RESOURCE_GROUP"),
            "project_name": os.environ.get("AZURE_PROJECT_NAME"),
        }
        self.evaluator = AzureProtectedMaterialEvaluator(
            azure_ai_project=azure_ai_project, credential=credential
        )

    def evaluate(self, query, response):
        return self.evaluator(query=query, response=response)
