import pandas as pd
from common.utils import load_data, save_data

def run_pipeline():
    # Load sample data
    data = load_data('data/samples/sample_data.csv')

    # Perform data transformations
    transformed_data = transform_data(data)

    # Save the transformed data
    save_data(transformed_data, 'data/samples/transformed_data.csv')

def transform_data(data):
    # Example transformation: filter and aggregate data
    filtered_data = data[data['value'] > 10]  # Filter rows where value > 10
    aggregated_data = filtered_data.groupby('category').sum()  # Aggregate by category
    return aggregated_data

if __name__ == "__main__":
    run_pipeline()