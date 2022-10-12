import ast
import pandas as pd
import re
import operator
from itertools import islice
import csv

# open file for chocolate bars
df = pd.read_csv('chocolate_bars.csv', usecols=['bean_origin'])
# print(df.head())

final_count = dict()

# go through sheet and count up number of origins for each country
for index, row in df.iterrows():
    curr_country = row["bean_origin"]
    if curr_country in final_count:
        final_count[curr_country] += 1
    else:
        final_count[curr_country] = 1

# fix up countries
final_count = {'Tanzania': 79, 'Dominican Rep.': 226, 'Madagascar': 177, 'Fiji': 16, 'Venezuela': 253, 'Uganda': 19, 'India': 35, 'Bolivia': 80, 'Peru': 244, 'Panama': 9, 'Colombia': 79, 'Myanmar': 1, 'Brazil': 78, 'Papua New Guinea': 50, 'Ecuador': 219, 'Cuba': 12, 'Togo': 3, 'Central African Rep.': 24, 'Mexico': 55, 'Vanuatu': 13, 'Indonesia': 21, 'Trinidad and Tobago': 44, 'Vietnam': 73, 'Nicaragua': 100, 'Ghana': 41, 'Belize': 76, 'Jamaica': 24, 'Guatemala': 62, 'Honduras': 25, 'Costa Rica': 43, 'Haiti': 30, 'Congo': 11, 'Philippines': 24, 'Solomon Is.': 10, 'Malaysia': 8, 'Sri Lanka': 2, 'Gabon': 1, 'Taiwan': 2, 'Puerto Rico': 7, 'Australia': 3, 'Liberia': 3, 'Sierra Leone': 4, 'United States of America': 33, 'Nigeria': 3, 'Thailand': 5, 'El Salvador': 6, 'Cameroon': 3, 'China': 1, 'Suriname': 1, 'Dem. Rep. Congo': 1}

# sort the countries in descending order
sorted_count = dict( sorted(final_count.items(), key=operator.itemgetter(1),reverse=True))

# create an object format in a list
gs_dict = []
for key in sorted_count:
    gs_dict.append({
    "bean_origin": key,
    "count": sorted_count[key],
})

# print(gs_dict)
# print(len(gs_dict)) # 62 countries in total

"""
Now working on adding latitude and longitude
"""
df2 = pd.read_csv('world_country_and_usa_states_latitude_and_longitude_values.csv', usecols=['country', 'longitude', 'latitude'])
# print(df2['country'].tolist())

countries_list = df2['country'].tolist()
detected_list = []
final_dict = []

for key in gs_dict:
    for index, row in df2.iterrows():
        if key['bean_origin'] == row['country']:
            final_dict.append({
                "bean_origin": key['bean_origin'],
                "count": key['count'],
                "longitude": row['longitude'],
                "latitude": row['latitude']
            })

print(len(final_dict))

# create and write new data to a new csv file
headers = ['bean_origin', 'count', 'longitude', 'latitude']
with open('bean_origin_data_count.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = headers)
    writer.writeheader()
    writer.writerows(final_dict)

# print(len(detected_list))
# print(len(gs_dict))

# create an object format in a list for the longitudes and latitudes as well
# full_dict = []
# for key in sorted_count:
#     gs_dict.append({
#     "bean_origin": key,
#     "count": sorted_count[key],
# })


# # create and write new data to a new csv file
# headers = ['bean_origin', 'count']
# with open('bean_origin_data_count.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames = headers)
#     writer.writeheader()
#     writer.writerows(gs_dict)
