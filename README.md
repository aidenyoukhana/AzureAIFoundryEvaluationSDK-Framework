# Azure AI Foundry Evaluation SDK - Python

This is a Python implementation of the Azure AI Foundry Evaluation SDK, organized into separate folders for different evaluator groups.

## Getting Started

### Step 1: Deploy Azure Resources

Deploy Azure AI Foundry Hub and GPT-4o using our automated script:

```bash
cd Infrastructure
./setup-interactive.sh
```

This will:
- Create Azure AI Foundry Hub in your subscription
- Deploy GPT-4o model
- Automatically generate your `.env` file with all credentials

📚 See [Infrastructure Deployment Guide](docs/infrastructure_deploy/) for detailed instructions.

**Already have Azure resources?** Skip to Step 2 and manually configure your `.env` file.

### Step 2: Setup Python Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Verify your `.env` file was created (or create it manually from `.env.example`)

## Running Tests

After setup, activate the virtual environment if not already active.

- **Run all tests with detailed output**: `pytest tests/ -v -s` (shows evaluation results in JSON format for each test case)
- **Run all tests**: `pytest` (this runs all test files in the `tests/` directory, covering all evaluators)
- **Run tests for a specific group**: `pytest tests/group_name/` (e.g., `pytest tests/general_purpose/`)
- **Run a specific test file**: `pytest tests/group_name/specific_test.py` (e.g., `pytest tests/general_purpose/coherence_test.py`)
- **Run a specific test function**: `pytest -k "test_function_name"` (e.g., `pytest -k "test_coherence_evaluator"`)

All tests read data from the corresponding JSONL files in `data/` and validate the evaluators without hardcoding.

## CI/CD

Data files in `data/` are used for testing. Ensure they are included in your GitHub repository for CI/CD pipelines.