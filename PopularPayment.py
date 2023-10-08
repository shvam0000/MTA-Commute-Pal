import pandas as pd
import json

# Load the dataset from the JSON URL
data_url = "https://data.ny.gov/resource/v7qc-gwpn.json"
data = pd.read_json(data_url)

data.drop(columns=['full_fare'], inplace=True)

# Group the data by the 'station' column and calculate the sum of integer-type columns
grouped_data = data.groupby('remote_station_id').sum(numeric_only=True)

# Find the top 3 columns with the highest sum for each station type
top_3_columns = grouped_data.apply(lambda x: x.nlargest(3).to_dict(), axis=1)

pay_dict = dict()

for i in top_3_columns.index:
    pay_dict.update({i: top_3_columns.loc[i]})

print(pay_dict)

# Save the JSON data to a file (you can change the filename as needed)
with open('most_popular_payment.json', 'w') as json_file:
    json.dump(pay_dict, json_file)

print("Top 3 Columns with Highest Sum for Each Station Type saved as 'most_popular_payment.json'")
