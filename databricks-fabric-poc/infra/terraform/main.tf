resource "databricks_cluster" "example" {
  cluster_name = "databricks-cluster"
  spark_version = "7.3.x-scala2.12"
  node_type_id = "i3.xlarge"
  num_workers = 2

  autoscale {
    min_workers = 1
    max_workers = 5
  }
}

resource "databricks_job" "example" {
  name = "sample-job"
  existing_cluster_id = databricks_cluster.example.id

  notebook_task {
    notebook_path = "/Users/example@databricks.com/demo_notebook"
  }
}

resource "azurerm_resource_group" "example" {
  name     = "example-resource-group"
  location = "East US"
}

resource "azurerm_data_factory" "example" {
  name                = "example-data-factory"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  sku {
    name     = "Basic"
    tier     = "Basic"
  }
}

resource "azurerm_data_factory_pipeline" "example" {
  name                = "sample-pipeline"
  data_factory_name   = azurerm_data_factory.example.name
  resource_group_name = azurerm_resource_group.example.name

  activities {
    name = "CopyData"
    type = "Copy"
    inputs {
      name = "inputDataset"
    }
    outputs {
      name = "outputDataset"
    }
  }
}