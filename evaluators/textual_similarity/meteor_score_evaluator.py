import os
from azure.ai.evaluation import MeteorScoreEvaluator as AzureMeteorScoreEvaluator
from dotenv import load_dotenv

load_dotenv()


class MeteorScoreEvaluator:
    def __init__(self):
        self.evaluator = AzureMeteorScoreEvaluator()

    def evaluate(self, response, ground_truth):
        return self.evaluator(response=response, ground_truth=ground_truth)
