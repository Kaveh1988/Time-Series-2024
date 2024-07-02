# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:34:36 2024

@author: kaveh
"""

import pandas as pd

def load_and_prepare_data(file_path):
    # Load JSON data into a pandas DataFrame
    data = pd.read_json(file_path)

    # Convert 'timestamp' from UNIX time to datetime
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')

    # Check for any missing values and handle them
    if data.isnull().any().any():
        print("Missing data found. Filling missing values with appropriate method...")
        # For simplicity, we can fill missing values with the mean of each column
        # This method should be tailored based on further analysis and understanding of the data
        data.fillna(data.mean(), inplace=True)

    # Ensure all data types are correct
    data['machine_id'] = data['machine_id'].astype(int)
    data['sensor_id'] = data['sensor_id'].astype(int)
    data['consumption_kwh'] = data['consumption_kwh'].astype(float)

    return data

# Example usage of the function
file_path = '/path/to/your/json1.json'
processed_data = load_and_prepare_data(file_path)
print(processed_data.head())  # Display the first few rows of the processed DataFrame
