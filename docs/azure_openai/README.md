# Azure OpenAI Evaluators

This folder contains custom graders built using Azure OpenAI models for various evaluation tasks.

## Graders

- **AzureOpenAIGrader**: A custom Python grader that calculates similarity between response and ground truth based on word overlap.
- **AzureOpenAILabelGrader**: Classifies responses into labels like "good" or "bad" using Azure OpenAI.
- **AzureOpenAIStringCheckGrader**: Checks if the input string matches certain criteria, such as starting with specific text.
- **AzureOpenAITextSimilarityGrader**: Evaluates text similarity using metrics like fuzzy match against a reference.