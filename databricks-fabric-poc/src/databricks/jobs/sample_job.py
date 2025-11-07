from pyspark.sql import SparkSession

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Sample Databricks Job") \
        .getOrCreate()

    # Load sample data
    df = spark.read.csv("/databricks/data/samples/sample_data.csv", header=True, inferSchema=True)

    # Perform some data transformations
    transformed_df = df.groupBy("column_name").count()

    # Show the results
    transformed_df.show()

    # Save the transformed data
    transformed_df.write.csv("/databricks/output/transformed_data.csv", header=True)

if __name__ == "__main__":
    main()