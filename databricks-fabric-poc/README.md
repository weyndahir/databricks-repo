# Databricks vs Microsoft Fabric POC

## Overview

This project serves as a proof of concept (POC) to compare the capabilities and performance of Databricks and Microsoft Fabric for data processing and analysis. The POC includes various components such as notebooks, jobs, pipelines, and infrastructure setup to evaluate both platforms effectively.

## Project Structure

The project is organized as follows:

- **src/**: Contains the source code for both Databricks and Microsoft Fabric implementations.
  - **databricks/**: Includes notebooks and jobs specific to Databricks.
  - **fabric/**: Includes notebooks and pipelines specific to Microsoft Fabric.
  - **common/**: Contains shared utilities and configuration settings.
  
- **tests/**: Contains unit tests that compare the functionalities and performance of Databricks and Microsoft Fabric.

- **infra/**: Contains infrastructure as code files for setting up the necessary resources.
  - **terraform/**: Terraform configuration files.
  - **arm_templates/**: Azure Resource Manager templates.

- **docs/**: Documentation files outlining architecture, runbook, and evaluation criteria.

- **data/**: Sample data used for testing and demonstration.

- **scripts/**: Shell scripts for environment setup and executing the POC.

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **README.md**: This documentation file.

- **requirements.txt**: Lists Python dependencies required for the project.

- **Dockerfile**: Defines the Docker image for the project.

- **.env.example**: Provides an example of environment variables needed for the project.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd databricks-fabric-poc
   ```

2. **Set Up the Environment**:
   Run the setup script to install dependencies and configure the environment:
   ```bash
   ./scripts/setup_env.sh
   ```

3. **Configure Environment Variables**:
   Copy the `.env.example` to `.env` and update the variables as needed.

4. **Run the POC**:
   Execute the POC by running the following script:
   ```bash
   ./scripts/run_poc.sh
   ```

## Evaluation Criteria

The evaluation of Databricks and Microsoft Fabric will be based on the following criteria:
- Performance metrics
- Ease of use
- Integration capabilities
- Cost-effectiveness

## Documentation

Refer to the documentation files in the `docs/` directory for detailed information on architecture, runbook, and evaluation criteria.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.