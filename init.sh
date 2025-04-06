#!/usr/bin/env bash

# Script to create the directory structure for the Yuanhua RWA MkDocs course

echo "Creating base directories..."
# Create main content directories under docs/
# The -p flag ensures parent directories are created if needed, and doesn't error if they exist
mkdir -p docs/part1
mkdir -p docs/part2
mkdir -p docs/part3
mkdir -p docs/resources
mkdir -p docs/assets # Directory for images and other static files

# Create GitHub Actions workflow directory
mkdir -p .github/workflows

echo "Creating core Markdown files..."
# Use 'touch' to create empty files. It won't overwrite existing files.
touch docs/index.md

echo "Creating Part 1 Markdown files..."
touch docs/part1/module1_intro.md
touch docs/part1/module2_tech.md

echo "Creating Part 2 Markdown files..."
touch docs/part2/module3_lifecycle.md
touch docs/part2/module4_finance.md
touch docs/part2/module5_compliance.md
touch docs/part2/module6_gomarket.md

echo "Creating Part 3 Markdown files..."
touch docs/part3/module7_deepdive.md
touch docs/part3/module8_invest.md
touch docs/part3/module9_future.md

# echo "Creating optional resource Markdown files..." # Uncomment if needed
# touch docs/resources/toolbox.md
# touch docs/resources/glossary.md

echo "Creating placeholder for GitHub Actions workflow file..."
touch .github/workflows/deploy.yml

# You might want a placeholder CNAME file if using a custom domain immediately
# echo "your-custom-domain.com" > docs/CNAME # Uncomment and replace with your domain if needed

echo "----------------------------------------"
echo "Directory structure created successfully!"
echo "Next steps:"
echo "1. Initialize MkDocs if you haven't: mkdocs new ."
echo "2. Configure your mkdocs.yml file (especially the 'nav' section)."
echo "3. Add content to the .md files."
echo "4. Add the deploy.yml content to .github/workflows/deploy.yml."
echo "----------------------------------------"

# List the created structure (optional, for verification)
echo "Current structure under docs/:"
ls -R docs/
echo "Current structure under .github/:"
ls -R .github/