class Config:
    def __init__(self):
        self.databricks_config = {
            'workspace_url': 'https://<your-databricks-workspace-url>',
            'token': '<your-databricks-token>',
            'cluster_id': '<your-cluster-id>',
        }
        self.fabric_config = {
            'workspace_url': 'https://<your-fabric-workspace-url>',
            'token': '<your-fabric-token>',
            'pipeline_id': '<your-pipeline-id>',
        }
        self.common_settings = {
            'data_path': '../data/samples/sample_data.csv',
            'log_level': 'INFO',
        }

    def get_databricks_config(self):
        return self.databricks_config

    def get_fabric_config(self):
        return self.fabric_config

    def get_common_settings(self):
        return self.common_settings