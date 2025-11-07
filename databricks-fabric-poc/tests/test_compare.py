# test_compare.py

import unittest
from src.common.utils import compare_performance
from src.databricks.jobs.sample_job import run_sample_job
from src.fabric.pipelines.sample_pipeline import run_sample_pipeline

class TestCompareDatabricksFabric(unittest.TestCase):

    def test_databricks_performance(self):
        databricks_result = run_sample_job()
        self.assertIsNotNone(databricks_result, "Databricks job did not return a result.")
        self.assertGreater(databricks_result['execution_time'], 0, "Databricks job execution time should be greater than 0.")

    def test_fabric_performance(self):
        fabric_result = run_sample_pipeline()
        self.assertIsNotNone(fabric_result, "Microsoft Fabric pipeline did not return a result.")
        self.assertGreater(fabric_result['execution_time'], 0, "Microsoft Fabric pipeline execution time should be greater than 0.")

    def test_performance_comparison(self):
        databricks_result = run_sample_job()
        fabric_result = run_sample_pipeline()
        
        comparison_result = compare_performance(databricks_result, fabric_result)
        self.assertIn('databricks', comparison_result, "Comparison result should include Databricks performance.")
        self.assertIn('fabric', comparison_result, "Comparison result should include Microsoft Fabric performance.")
        self.assertTrue(comparison_result['databricks']['execution_time'] >= comparison_result['fabric']['execution_time'],
                        "Databricks should perform better or equal to Microsoft Fabric.")

if __name__ == '__main__':
    unittest.main()