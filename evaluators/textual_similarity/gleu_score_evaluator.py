import os
from azure.ai.evaluation import GleuScoreEvaluator as AzureGleuScoreEvaluator
from dotenv import load_dotenv

load_dotenv()


class GleuScoreEvaluator:
    def __init__(self):
        self.evaluator = AzureGleuScoreEvaluator()

    def evaluate(self, response, ground_truth):
        return self.evaluator(response=response, ground_truth=ground_truth)
