# GenAI Evals Format Data

This directory contains evaluation data formatted specifically for the Microsoft `genai-evals` GitHub Action.

## Format Requirements

The `genai-evals` GitHub Action requires JSONL data with a specific structure:

```json
{
  "inputs": {
    "query": "The input query/question",
    "context": "Optional context for RAG scenarios"
  },
  "outputs": {
    "response": "The model's response to evaluate"
  },
  "description": {
    "context": {
      "system-prompt": "The system prompt used for the test variant"
    }
  }
}
```

## Key Differences from Standard Format

The standard Azure AI Evaluation SDK format uses top-level keys like `query`, `response`, `context`.

The GitHub Action format requires:
1. **inputs** object - Contains `query` and optionally `context`
2. **outputs** object - Contains `response`
3. **description** object - Must have a nested structure with `context.system-prompt` for the summary visualization

## Converting Data

To convert data from the standard format to genai-evals format, run:

```bash
python3 convert_to_genai_evals_format.py
```

This script will:
- Read files from `data/general_purpose/`
- Convert them to the genai-evals format
- Save them in `data/genai_evals_format/`

## Why Two Formats?

- **Standard format** (`data/general_purpose/`): Used for local evaluations with the Azure AI Evaluation SDK
- **GenAI evals format** (`data/genai_evals_format/`): Required for GitHub Actions CI/CD pipeline

This allows the same test data to work both locally and in CI/CD.
