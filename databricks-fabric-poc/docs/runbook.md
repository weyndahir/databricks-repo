# Runbook for Databricks and Microsoft Fabric POC

## Overview

This runbook provides step-by-step instructions for setting up and executing the proof of concept (POC) project that compares Databricks and Microsoft Fabric. The goal of this POC is to evaluate the capabilities and performance of both platforms in data processing and analysis.

## Prerequisites

Before proceeding, ensure that you have the following:

- Access to Databricks and Microsoft Fabric environments.
- Necessary permissions to create and manage resources in both platforms.
- Installed dependencies as specified in `requirements.txt`.

## Setup Instructions

1. **Clone the Repository**

   Clone the project repository to your local machine:

   ```bash
   git clone <repository-url>
   cd databricks-fabric-poc
   ```

2. **Set Up Environment**

   Run the setup script to install the required dependencies:

   ```bash
   chmod +x scripts/setup_env.sh
   ./scripts/setup_env.sh
   ```

3. **Configure Environment Variables**

   Create a `.env` file based on the provided `.env.example`:

   ```bash
   cp .env.example .env
   ```

   Update the `.env` file with your specific configuration settings for Databricks and Microsoft Fabric.

4. **Deploy Infrastructure**

   Use Terraform to deploy the necessary infrastructure for the POC:

   ```bash
   cd infra/terraform
   terraform init
   terraform apply
   ```

5. **Run the POC**

   Execute the POC by running the provided script:

   ```bash
   chmod +x scripts/run_poc.sh
   ./scripts/run_poc.sh
   ```

## Execution Steps

### Databricks

1. **Run the Databricks Notebook**

   Open the `src/databricks/notebooks/demo_notebook.ipynb` in your Databricks workspace and execute the cells to see the data processing and analysis examples.

2. **Execute the Sample Job**

   Run the `src/databricks/jobs/sample_job.py` script in your Databricks environment to perform data transformations.

### Microsoft Fabric

1. **Run the Microsoft Fabric Notebook**

   Open the `src/fabric/notebooks/demo_notebook.ipynb` in your Microsoft Fabric workspace and execute the cells to view the examples.

2. **Execute the Sample Pipeline**

   Run the `src/fabric/pipelines/sample_pipeline.py` script in your Microsoft Fabric environment to orchestrate data workflows.

## Evaluation

After executing the notebooks and jobs, refer to `tests/test_compare.py` to run the unit tests that compare the functionalities and performance of Databricks and Microsoft Fabric. This will help in assessing which platform meets the evaluation criteria outlined in `docs/evaluation_criteria.md`.

## Conclusion

This runbook serves as a guide to successfully set up and execute the POC comparing Databricks and Microsoft Fabric. For further details on architecture and evaluation criteria, please refer to the respective documentation files in the `docs` directory.