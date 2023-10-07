import pandas as pd
import requests
import json

# Load the ridership data from the JSON URL
ridership_url = "https://data.ny.gov/resource/wujg-7c2s.json"
ridership_data = pd.read_json(ridership_url)

# Group the data by station ID and payment method, and calculate total ridership
grouped_data = ridership_data.groupby(['station_complex_id', 'payment_method'])['ridership'].sum().reset_index()

# Find the payment method with the highest ridership for each station ID
most_popular_payment = grouped_data.groupby('station_complex_id')['ridership'].idxmax()
most_popular_payment_data = grouped_data.loc[most_popular_payment]

# Convert the result to a JSON format and save it to a file
result_json = most_popular_payment_data.to_json(orient='records', indent=4)

# Save the JSON data to a file (you can change the filename as needed)
with open('most_popular_payment.json', 'w') as json_file:
    json_file.write(result_json)

print("Most Popular Payment Method for Each Station ID saved as 'most_popular_payment.json'")
