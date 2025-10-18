# Infrastructure Setup

This directory contains infrastructure-as-code (IaC) files for deploying Azure AI Foundry Hub with GPT-4o model deployment.

## 📁 Files

- **`setup-interactive.sh`** - Interactive Bash script that guides you through the deployment process
- **`azure-ai-foundry-setup.bicep`** - Bicep template defining the Azure resources
- **`DEPLOYMENT_GUIDE.md`** - Comprehensive deployment documentation

## 🚀 Quick Start

```bash
# Make sure you're in the Infrastructure directory
cd Infrastructure

# Run the interactive setup
./setup-interactive.sh
```

The script will:
1. Check your Azure login
2. Let you select a subscription
3. Prompt for resource configuration
4. Deploy Azure AI Foundry Hub + GPT-4o
5. **Automatically create `.env` file** with all configuration

## ✨ What Gets Created

### Azure Resources
- **Resource Group** in East US 2
- **Azure AI Services Account** (S0 SKU)
- **GPT-4o Model Deployment** (Standard, 10 TPM)

### Configuration File
A `.env` file is automatically created at the project root with:
- Azure OpenAI endpoint
- GPT-4o deployment name
- API key
- Subscription and resource group details

## 📋 Example

```bash
$ ./setup-interactive.sh

Enter Resource Group name: MyAIProject
Enter Owner tag: user@example.com
Enter Azure AI Foundry Hub name: MyAIProject

Creating resource group...
Deploying resources...
✅ Deployment completed!

Creating .env file at ../.env...
✅ .env file created successfully!

🎉 Setup Complete!
```

## 🔐 Security

- `.env` file is automatically added to `.gitignore`
- Never commit API keys to version control
- Use Azure Key Vault for production environments

## 📖 Documentation

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed instructions and troubleshooting.

## 🛠️ Manual Deployment

If you prefer manual deployment:

```bash
# Login to Azure
az login

# Set subscription
az account set --subscription <subscription-id>

# Create resource group
az group create --name <rg-name> --location eastus2

# Deploy using Bicep
az deployment group create \
  --resource-group <rg-name> \
  --template-file azure-ai-foundry-setup.bicep \
  --parameters hubName=<hub-name> location=eastus2 ownerTag=<your-email>
```

## 🧹 Cleanup

To delete all resources:

```bash
az group delete --name <resource-group-name> --yes --no-wait
```

## ❓ Troubleshooting

### Common Issues

**"The content for this response was already consumed"**
- This was a known issue with the old script version
- The updated script resolves this problem

**Quota errors**
```bash
# Check your quota
az cognitiveservices usage list --location eastus2
```

**Deployment fails**
- Verify you have sufficient permissions
- Check if GPT-4o is available in your region
- Ensure you have available quota

### Getting Help

1. Review the verbose deployment output
2. Check [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
3. View resources in Azure Portal
4. Check Azure Service Health

## 🎯 Next Steps

After deployment:
1. ✅ Verify `.env` file exists in project root
2. ✅ Install dependencies: `pip install -r ../requirements.txt`
3. ✅ Run evaluators from the project root
4. ✅ Monitor usage in Azure Portal
