import os
from azure.ai.evaluation import F1ScoreEvaluator as AzureF1ScoreEvaluator
from dotenv import load_dotenv

load_dotenv()


class F1ScoreEvaluator:
    def __init__(self):
        self.evaluator = AzureF1ScoreEvaluator()

    def evaluate(self, response, ground_truth):
        return self.evaluator(response=response, ground_truth=ground_truth)
