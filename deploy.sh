#!/bin/bash

#cd /home/hero/CI-CD_Pipeline_Tool/
sudo rm -rf /var/www/html
# Define your GitHub repository URL
GITHUB_REPO_URL="https://github.com/AdarshIITDH/CI-CD_Pipeline_Tool.git"

# Directory where you want to deploy the code
DEPLOY_DIR="/var/www/html"

# Clone the latest code
git clone $GITHUB_REPO_URL $DEPLOY_DIR

# Restart Nginx
sudo systemctl restart nginx
