import pandas as pd

df = pd.read_csv("MTA_Subway_Hourly_Ridership__Beginning_February_2022.csv")
df2 = pd.read_csv('Fare_Card_History_for_Metropolitan_Transportation_Authority__MTA___Beginning_2010.csv')

unique_df = df.groupby(["station_complex_id"]).first()#.set_index('station_complex_id')
unique_df2 = df2.groupby(["Remote Station ID"]).sum(numeric_only=True)#.set_index('Remote Station ID')

merged_geo_data_df = pd.merge(unique_df, unique_df2, left_index=True, right_index=True, how='inner')
final_json = dict()
for i in merged_geo_data_df.index:
    Payment_mode = merged_geo_data_df.loc[i][[ 'Senior Citizen / Disabled',
       '7 Day ADA Farecard Access System Unlimited',
       '30 Day ADA Farecard Access System Unlimited', 'Joint Rail Road Ticket',
       '7 Day Unlimited', '30 Day Unlimited',
       '14 Day Reduced Fare Media Unlimited', '1 Day Unlimited',
       '14 Day Unlimited', '7 Day Express Bus Pass', 'Transit Check Metrocard',
       'LIB Special Senior', 'Rail Road Unlimited No Trade',
       'Transit Check Metrocard Annual Metrocard',
       'Mail and Ride Easy Pay Express', 'Mail and Ride Unlimited',
       'Path 2 Trip', 'Airtran Full Fare', 'Airtran 30 Day', 'Airtran 10 Trip',
       'Airtran Monthly']].astype(int).nlargest(3).to_dict()
    payment_mode_final = dict(zip(range(3),Payment_mode.keys()))
    payment_mode_final.update(dict(zip(range(3,6),Payment_mode.values())))
    payment_mode_final.update({'latitude':merged_geo_data_df.loc[i]['latitude'], 'longitude':merged_geo_data_df.loc[i]['longitude']})
    final_json.update({i:payment_mode_final})

import json
with open('most_popular_payment.json', 'w') as f:
    json.dump(final_json, f)

# ---------------------------


payment_station = merged_geo_data_df[['Senior Citizen / Disabled',
       '7 Day ADA Farecard Access System Unlimited',
       '30 Day ADA Farecard Access System Unlimited', 'Joint Rail Road Ticket',
       '7 Day Unlimited', '30 Day Unlimited',
       '14 Day Reduced Fare Media Unlimited', '1 Day Unlimited',
       '14 Day Unlimited', '7 Day Express Bus Pass', 'Transit Check Metrocard',
       'LIB Special Senior', 'Rail Road Unlimited No Trade',
       'Transit Check Metrocard Annual Metrocard',
       'Mail and Ride Easy Pay Express', 'Mail and Ride Unlimited',
       'Path 2 Trip', 'Airtran Full Fare', 'Airtran 30 Day', 'Airtran 10 Trip',
       'Airtran Monthly']]#.to_dict('index')

payment_modes = ['Senior Citizen / Disabled',
       '7 Day ADA Farecard Access System Unlimited',
       '30 Day ADA Farecard Access System Unlimited', 'Joint Rail Road Ticket',
       '7 Day Unlimited', '30 Day Unlimited',
       '14 Day Reduced Fare Media Unlimited', '1 Day Unlimited',
       '14 Day Unlimited', '7 Day Express Bus Pass', 'Transit Check Metrocard',
       'LIB Special Senior', 'Rail Road Unlimited No Trade',
       'Transit Check Metrocard Annual Metrocard',
       'Mail and Ride Easy Pay Express', 'Mail and Ride Unlimited',
       'Path 2 Trip', 'Airtran Full Fare', 'Airtran 30 Day', 'Airtran 10 Trip',
       'Airtran Monthly']

payment_station_json=dict()
for i in (payment_modes):
    temp_dict = dict()
    for j in merged_geo_data_df[i].index:
        temp_dict.update({str(j):{'count':merged_geo_data_df.loc[j,i], 'latitude':merged_geo_data_df.loc[j,'latitude'],'longitude':merged_geo_data_df.loc[j,'longitude']}})
    
    payment_station_json.update({str(i):temp_dict})

print(payment_station_json)
# import json
# with open('payment_station_mapping.json', 'w') as f:
#     json.dump(payment_station_json, f)
