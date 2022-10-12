import ast
import pandas as pd
import re
import operator
from itertools import islice
import csv

# open file for chocolate bars
df = pd.read_csv('bar-chart/chocolate_bars.csv', usecols=['manufacturer', 'company_location'])
# print(df.head())

# go through each company_location and count up the manufacturers
count_dict = {}
man_already = []

for index, row in df.iterrows():
    curr_comp_man = row['company_location'] + "$" + row['manufacturer']
    if curr_comp_man in count_dict:
        count_dict[curr_comp_man] += 1
    else:
        count_dict[curr_comp_man] = 1

# print(count_dict)

# count up the manufacturers for each country
country_count_dict = {}

for key in count_dict:
    country_str = key.partition('$')[0]
    if country_str in country_count_dict:
        country_count_dict[country_str] += 1
    else:
        country_count_dict[country_str] = 1

# sort the countries in descending order and get top 10 countries with mans
sorted_count = dict( sorted(country_count_dict.items(), key=operator.itemgetter(1),reverse=True))
dict_items = sorted_count.items()
top_10_man_list = list(dict_items)[:10]

gs_dict = []
for country in top_10_man_list:
    gs_dict.append({
        "country": country[0],
        "manufacturer_count": country[1]
    })

print(gs_dict)

# create and write new data to a new csv file
headers = ['country', 'manufacturer_count']
with open('country_manufacturer_data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = headers)
    writer.writeheader()
    writer.writerows(gs_dict)
