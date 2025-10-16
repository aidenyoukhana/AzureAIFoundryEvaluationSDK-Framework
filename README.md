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

## CI/CD with GitHub Actions

This repository includes a GitHub Actions workflow (`.github/workflows/evaluate.yml`) that automatically runs AI evaluations on push to main or via manual trigger.

### Setting Up GitHub Actions

To enable the CI/CD pipeline, you need to configure GitHub secrets and create an Azure App Registration for authentication.

#### Step 1: Create Azure App Registration

1. **Go to Azure Portal** → **Azure Active Directory** → **App registrations** → **New registration**
   - Name: `github-actions-aafesdk-eval` (or your preferred name)
   - Click **Register**

2. **Create a client secret:**
   - Go to **Certificates & secrets** → **New client secret**
   - Add a description (e.g., "GitHub Actions")
   - Set expiration (recommended: 90 days or as per your security policy)
   - Click **Add**
   - **⚠️ Important**: Copy the **Value** immediately - you won't be able to see it again

3. **Note the following values** (you'll need them for GitHub secrets):
   - **Application (client) ID** - found on the app registration Overview page
   - **Directory (tenant) ID** - found on the app registration Overview page
   - **Client secret Value** - the value you just copied

#### Step 2: Assign IAM Role to Resource Group

1. **Go to Azure Portal** → **Resource Groups** → Select your resource group (e.g., `AAFESDK-Framework-RG`)

2. **Click Access control (IAM)** → **Add role assignment**

3. **Select role: Azure AI Developer**
   - This role provides the necessary permissions to access AI services and deployments

4. **Assign access to:**
   - Select **User, group, or service principal**
   - Click **Select members**
   - Search for your app registration name (e.g., `github-actions-aafesdk-eval`)
   - Select it and click **Select**

5. **Click Review + assign** (twice)

#### Step 3: Configure GitHub Secrets

Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Add the following **8 secrets**:

| Secret Name | Description | Example Value |
|------------|-------------|---------------|
| `AZURE_CLIENT_ID` | Application (client) ID from your App Registration | `12345678-1234-1234-1234-123456789abc` |
| `AZURE_CLIENT_SECRET` | Client secret value from your App Registration | `abc123~defghijklmnop` |
| `AZURE_TENANT_ID` | Directory (tenant) ID from your App Registration | `12345678-1234-1234-1234-123456789abc` |
| `AZURE_SUBSCRIPTION_ID` | Your Azure subscription ID | `12345678-1234-1234-1234-123456789abc` |
| `AZURE_OPENAI_API_KEY` | API key from your Azure AI Services resource | Found in Azure Portal under your AI Services resource → Keys and Endpoint |
| `AZURE_OPENAI_API_VERSION` | Azure OpenAI API version | `2024-12-01-preview` |
| `AZURE_OPENAI_DEPLOYMENT_NAME` | Name of your model deployment | `gpt-4o` |
| `AZURE_OPENAI_ENDPOINT` | Endpoint URL of your Azure AI Services | `https://your-resource-name.cognitiveservices.azure.com/` |

**To get the Azure OpenAI values:**
- Run the setup script if you haven't: `cd Infrastructure && ./setup-interactive.sh`
- Or check your `.env` file in the project root
- Or get them from Azure Portal → Your AI Services resource → **Keys and Endpoint**

#### Step 4: Verify the Workflow

Once secrets are configured, the workflow will automatically run:
- On every push to the `main` branch
- Manually via **Actions** tab → **AI Evaluation** → **Run workflow**

The workflow will:
1. Authenticate to Azure using the service principal
2. Run AI evaluations using the configured evaluators
3. Display results in the Actions log

### Troubleshooting GitHub Actions

**Error: "Application with identifier '***' was not found"**
- Verify `AZURE_CLIENT_ID` matches your App Registration's Application (client) ID
- Verify `AZURE_TENANT_ID` is correct
- Ensure the App Registration exists in the correct Azure AD tenant

**Error: "Forbidden" or "Access Denied"**
- Verify the App Registration has the **Azure AI Developer** role assigned to your resource group
- Wait a few minutes for role assignments to propagate

**Error: "Resource not found" or "Deployment not found"**
- Verify `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT_NAME` are correct
- Ensure the deployment exists in your Azure AI Services resource

Data files in `data/` are used for testing. Ensure they are included in your GitHub repository for CI/CD pipelines.
