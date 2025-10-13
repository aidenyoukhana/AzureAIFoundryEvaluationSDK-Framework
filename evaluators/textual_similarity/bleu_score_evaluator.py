import os
from azure.ai.evaluation import BleuScoreEvaluator as AzureBleuScoreEvaluator
from dotenv import load_dotenv

load_dotenv()


class BleuScoreEvaluator:
    def __init__(self):
        self.evaluator = AzureBleuScoreEvaluator()

    def evaluate(self, response, ground_truth):
        return self.evaluator(response=response, ground_truth=ground_truth)
