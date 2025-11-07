# Architecture of the Databricks and Microsoft Fabric POC

## Overview

This document outlines the architecture of the proof of concept (POC) project that compares Databricks and Microsoft Fabric. The POC aims to evaluate the capabilities, performance, and integration of both platforms for data processing and analysis.

## Architecture Components

### 1. Data Sources

The POC utilizes sample data stored in the `data/samples/sample_data.csv` file. This data serves as the input for both Databricks and Microsoft Fabric workflows.

### 2. Data Processing Frameworks

- **Databricks**: 
  - Utilizes notebooks located in `src/databricks/notebooks/demo_notebook.ipynb` for interactive data analysis and visualization.
  - Executes jobs defined in `src/databricks/jobs/sample_job.py` to perform data transformations and analyses.

- **Microsoft Fabric**: 
  - Employs notebooks found in `src/fabric/notebooks/demo_notebook.ipynb` for similar data processing tasks.
  - Implements data pipelines defined in `src/fabric/pipelines/sample_pipeline.py` to orchestrate data workflows.

### 3. Common Utilities

The project includes shared utility functions and configuration management through:
- `src/common/utils.py`: Contains utility functions used across both platforms.
- `src/common/config.py`: Manages configuration settings for the POC, allowing for easy adjustments.

### 4. Infrastructure

The infrastructure for the POC is defined using:
- **Terraform**: The configuration file located at `infra/terraform/main.tf` specifies the resources required for both Databricks and Microsoft Fabric.
- **Azure Resource Manager (ARM) Templates**: The `infra/arm_templates/deployment.json` file contains templates for deploying necessary resources in Azure.

### 5. Testing and Evaluation

The project includes a testing framework to compare the functionalities and performance of both platforms:
- `tests/test_compare.py`: Contains unit tests that evaluate the performance and capabilities of Databricks versus Microsoft Fabric based on predefined criteria.

### 6. Execution Scripts

To facilitate the execution of the POC, the following scripts are provided:
- `scripts/setup_env.sh`: Sets up the environment by installing dependencies and configuring settings.
- `scripts/run_poc.sh`: Executes the POC, running the necessary jobs and pipelines in both Databricks and Microsoft Fabric.

## Conclusion

This architecture provides a comprehensive framework for evaluating Databricks and Microsoft Fabric in a controlled environment. By leveraging shared utilities, infrastructure as code, and a structured testing approach, the POC aims to deliver insights into the strengths and weaknesses of each platform for data processing and analysis tasks.