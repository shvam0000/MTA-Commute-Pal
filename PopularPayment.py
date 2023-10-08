import pandas as pd
import requests

# Load the dataset from the JSON URL
data_url = "https://data.ny.gov/resource/v7qc-gwpn.json"
data = pd.read_json(data_url)

# Group the data by the 'station' column and calculate the sum of integer-type columns
grouped_data = data.groupby('remote_station_id').sum(numeric_only=True)

# Find the column with the highest sum for each station type
highest_value_column = grouped_data.idxmax(axis=1)

print(highest_value_column)
# Determine the most popular station type
most_popular_station_type = highest_value_column.value_counts().idxmax()

print("Most Popular Station Type:", most_popular_station_type)
