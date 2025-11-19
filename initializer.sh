#!/bin/bash

# Exits Immediately If a Command Fails
set -e

# Creating a Virtual Environment
echo "Setting up python environment"
python -m venv .venv
source .venv/Scripts/activate

# Installing Dependencies and Starting Flask Application
echo "Installing requirements, if successful Starting Flask Application"
pip install -r requirements.txt && python flask run

