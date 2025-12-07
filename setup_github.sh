#!/bin/bash

# 1. Initialize Git
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
    git branch -M main
else
    echo "Git repository already initialized."
fi

# 2. Add files
echo "Adding files..."
git add .

# 3. Commit
echo "Committing files..."
git commit -m "Initial commit of Shivhare Bangle Store"

# 4. Instructions
echo ""
echo "--------------------------------------------------------"
echo "Success! Local repository is ready."
echo "--------------------------------------------------------"
echo "To push to GitHub, run these two commands:"
echo ""
echo "  1. git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git"
echo "  2. git push -u origin main"
echo ""
echo "--------------------------------------------------------"
