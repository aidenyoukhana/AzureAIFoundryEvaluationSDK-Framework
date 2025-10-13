import os
from azure.ai.evaluation import RougeScoreEvaluator as AzureRougeScoreEvaluator
from dotenv import load_dotenv

load_dotenv()


class RougeScoreEvaluator:
    def __init__(self):
        self.evaluator = AzureRougeScoreEvaluator("rouge1")

    def evaluate(self, response, ground_truth):
        return self.evaluator(response=response, ground_truth=ground_truth)
