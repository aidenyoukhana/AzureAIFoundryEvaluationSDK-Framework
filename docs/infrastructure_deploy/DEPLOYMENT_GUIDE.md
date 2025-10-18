# Azure AI Foundry Deployment Guide

## Overview

This guide explains how to use the interactive setup script to deploy Azure AI Foundry Hub with GPT-4o and automatically generate your `.env` configuration file.

## Prerequisites

- Azure CLI installed and configured
- Bash shell (macOS/Linux) or WSL on Windows
- An active Azure subscription
- Appropriate permissions to create resources in Azure

## Quick Start

1. Navigate to the Infrastructure directory:
   ```bash
   cd Infrastructure
   ```

2. Make the script executable (if needed):
   ```bash
   chmod +x setup-interactive.sh
   ```

3. Run the interactive setup:
   ```bash
   ./setup-interactive.sh
   ```

## What the Script Does

The script will:

1. ✅ Check your Azure login status
2. ✅ List available subscriptions and let you choose one
3. ✅ Prompt for configuration details:
   - Resource Group name
   - Owner tag (your email)
   - Azure AI Foundry Hub name
4. ✅ Create the Resource Group in East US 2
5. ✅ Deploy Azure AI Services with GPT-4o model
6. ✅ Retrieve all necessary configuration details:
   - Endpoint URL
   - Deployment name
   - API key
   - Subscription ID
7. ✅ **Automatically create a `.env` file** in the project root with all configuration

## Generated .env File

After successful deployment, a `.env` file will be created at the project root with:

```properties
# Azure OpenAI Configuration (for RAG, General Purpose, and Agentic evaluators)
AZURE_OPENAI_ENDPOINT=https://your-hub-name.cognitiveservices.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_API_KEY=your-api-key-here

# Azure AI Foundry Project Configuration (for Risk/Safety evaluators)
# Hub and Project created in East US 2 for full evaluator support
AZURE_SUBSCRIPTION_ID=your-subscription-id
AZURE_RESOURCE_GROUP=your-resource-group-name
AZURE_PROJECT_NAME=your-ai-foundry-hub-name
```

## Example Output

```
================================================
Configuration Retrieved Successfully!
================================================

AZURE_OPENAI_ENDPOINT=https://aidentest4.cognitiveservices.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_API_KEY=******************

AZURE_SUBSCRIPTION_ID=f908d274-fb43-4af6-8fb6-614bf5fdfb94
AZURE_RESOURCE_GROUP=AidenTest4
AZURE_PROJECT_NAME=AidenTest4

Creating .env file at ../.env...

✅ .env file created successfully at: ../.env

================================================
🎉 Setup Complete!
================================================

Your Azure AI Foundry Hub is ready to use!
All configuration has been saved to .env file.

Resource Group: AidenTest4
AI Foundry Hub: AidenTest4
Endpoint: https://aidentest4.cognitiveservices.azure.com/
Deployment: gpt-4o
```

## Deployed Resources

The Bicep template creates:

1. **Azure AI Services Account** (`Microsoft.CognitiveServices/accounts`)
   - Kind: AIServices
   - SKU: S0 (Standard)
   - Region: East US 2
   - Features: API key and Azure AD authentication enabled

2. **GPT-4o Model Deployment** (`Microsoft.CognitiveServices/accounts/deployments`)
   - Model: gpt-4o (version 2024-08-06)
   - SKU: Standard
   - Capacity: 10 TPM (Tokens Per Minute)

## Configuration Details

### API Version
- Using `2024-12-01-preview` for the latest features
- Compatible with Azure OpenAI SDK v1.x

### Authentication
- `disableLocalAuth: false` - Allows API key authentication
- Also supports Azure AD authentication

### Capacity
- Standard SKU with 10 TPM minimum
- Can be increased based on quota limits

## Troubleshooting

### Quota Issues
If you encounter quota errors:
```bash
# Check your quota
az cognitiveservices usage list --location eastus2

# Request quota increase through Azure Portal
```

### Region Availability
If the deployment fails due to region availability:
1. Edit `azure-ai-foundry-setup.bicep`
2. Change the default location parameter
3. Update the script to use a different region

### API Key Not Retrieved
If the API key retrieval fails:
```bash
# Manually get the key
az cognitiveservices account keys list \
  --name <your-hub-name> \
  --resource-group <your-rg-name>
```

## Manual Cleanup

To delete the resources:
```bash
az group delete --name <your-resource-group-name> --yes --no-wait
```

## Next Steps

After successful deployment:

1. ✅ Verify the `.env` file in the project root
2. ✅ Install Python dependencies: `pip install -r requirements.txt`
3. ✅ Run evaluators using the configuration
4. ✅ Check Azure Portal to view your resources

## Security Notes

⚠️ **Important**: The `.env` file contains sensitive information (API keys)
- Never commit `.env` to version control
- Add `.env` to your `.gitignore` file
- Rotate keys regularly in production environments
- Use Azure Key Vault for production deployments

## Support

For issues or questions:
- Check Azure Portal for resource status
- Review deployment logs with `--verbose` flag
- Contact your Azure administrator for quota/permission issues
