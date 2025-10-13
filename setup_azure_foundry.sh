#!/bin/bash
# Azure AI Foundry Setup Script
# This script creates the required Azure AI Foundry infrastructure for Risk/Safety evaluators

set -e  # Exit on error

echo "🚀 Azure AI Foundry Setup for Risk/Safety Evaluators"
echo "=================================================="
echo ""

# Configuration from your .env
SUBSCRIPTION_ID="f908d274-fb43-4af6-8fb6-614bf5fdfb94"
RESOURCE_GROUP="microsoft-agent-framework-playground"
HUB_NAME="maf-playground-hub"
PROJECT_NAME="maf-playground"
LOCATION="eastus"

echo "📋 Configuration:"
echo "  Subscription: $SUBSCRIPTION_ID"
echo "  Resource Group: $RESOURCE_GROUP"
echo "  Location: $LOCATION"
echo "  Hub: $HUB_NAME"
echo "  Project: $PROJECT_NAME"
echo ""

# Step 1: Install/Update Azure ML Extension
echo "Step 1/3: Installing Azure ML extension..."
az extension add --name ml --upgrade --only-show-errors
echo "✅ Extension installed"
echo ""

# Step 2: Create Azure AI Foundry Hub
echo "Step 2/3: Creating Azure AI Foundry Hub..."
if az ml workspace show --name "$HUB_NAME" --resource-group "$RESOURCE_GROUP" &>/dev/null; then
    echo "⚠️  Hub '$HUB_NAME' already exists, skipping..."
else
    az ml workspace create \
        --kind hub \
        --name "$HUB_NAME" \
        --resource-group "$RESOURCE_GROUP" \
        --location "$LOCATION" \
        --subscription "$SUBSCRIPTION_ID" \
        --only-show-errors
    echo "✅ Hub created successfully"
fi
echo ""

# Step 3: Create Azure AI Foundry Project
echo "Step 3/3: Creating Azure AI Foundry Project..."
if az ml workspace show --name "$PROJECT_NAME" --resource-group "$RESOURCE_GROUP" &>/dev/null; then
    echo "⚠️  Project '$PROJECT_NAME' already exists, skipping..."
else
    HUB_ID="/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$HUB_NAME"
    
    az ml workspace create \
        --kind project \
        --name "$PROJECT_NAME" \
        --resource-group "$RESOURCE_GROUP" \
        --location "$LOCATION" \
        --hub-id "$HUB_ID" \
        --subscription "$SUBSCRIPTION_ID" \
        --only-show-errors
    echo "✅ Project created successfully"
fi
echo ""

# Verification
echo "🔍 Verifying setup..."
echo ""
echo "Hub details:"
az ml workspace show --name "$HUB_NAME" --resource-group "$RESOURCE_GROUP" --output table --only-show-errors
echo ""
echo "Project details:"
az ml workspace show --name "$PROJECT_NAME" --resource-group "$RESOURCE_GROUP" --output table --only-show-errors
echo ""

echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Run all tests: pytest tests/ -v"
echo "  2. Run just Risk/Safety: pytest tests/risk_safety/ -v"
echo ""
echo "Expected result: All 31 tests should now pass ✅"
