#!/bin/bash

# This script sets up the environment for the Databricks and Microsoft Fabric POC project.

# Update package lists
sudo apt update

# Install necessary dependencies
sudo apt install -y python3 python3-pip

# Install Python packages from requirements.txt
pip3 install -r ../requirements.txt

# Additional setup can be added here, such as configuring environment variables or installing other tools

echo "Environment setup complete."