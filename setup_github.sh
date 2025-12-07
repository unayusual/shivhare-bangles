#!/bin/bash

# 1. Initialize Git (if needed)
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
    git branch -M main
    git add .
    git commit -m "Initial commit of Shivhare Bangle Store"
else
    echo "Git repository already initialized."
fi

# 2. Check if remote exists
if git remote | grep -q 'origin'; then
    echo "Remote 'origin' already exists."
    echo "Removing old origin to ensure we use the correct one..."
    git remote remove origin
fi

# 3. Prompt for URL
echo ""
echo "----------------------------------------------------------------"
echo "IMPORTANT: You must create a new EMPTY repository on GitHub.com"
echo "Go to https://github.com/new and create one now."
echo "----------------------------------------------------------------"
echo ""
read -p "Paste your HTTPS Repository URL here (e.g., https://github.com/unayusual/repo.git): " REPO_URL

if [ -z "$REPO_URL" ]; then
    echo "No URL provided. Exiting."
    exit 1
fi

# 4. Add Remote and Push
echo ""
echo "Setting remote to: $REPO_URL"
git remote add origin "$REPO_URL"

echo "Attempting to push code..."
echo "NOTE: When promised for Password, use your Personal Access Token (NOT your Google password)."
echo ""
git push -u origin main

echo ""
echo "--------------------------------------------------------"
echo "If the push succeeded, your site is now on GitHub!"
echo "If it failed due to authentication, you need a Token:"
echo "https://github.com/settings/tokens"
echo "--------------------------------------------------------"
