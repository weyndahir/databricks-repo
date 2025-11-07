#!/bin/bash

# This script executes the proof of concept (POC) for comparing Databricks and Microsoft Fabric.

# Set environment variables
source ./scripts/setup_env.sh

# Run Databricks job
echo "Running Databricks job..."
python src/databricks/jobs/sample_job.py

# Check if the Databricks job was successful
if [ $? -ne 0 ]; then
    echo "Databricks job failed."
    exit 1
fi

# Run Microsoft Fabric pipeline
echo "Running Microsoft Fabric pipeline..."
python src/fabric/pipelines/sample_pipeline.py

# Check if the Microsoft Fabric pipeline was successful
if [ $? -ne 0 ]; then
    echo "Microsoft Fabric pipeline failed."
    exit 1
fi

echo "POC execution completed successfully."