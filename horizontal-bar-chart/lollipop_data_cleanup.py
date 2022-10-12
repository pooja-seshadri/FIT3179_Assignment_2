import ast
import pandas as pd
import re
import operator
from itertools import islice
import csv

# open file for reading
df = pd.read_csv('data/chocolate_bars.csv', usecols=['review'])
# print(df.head())

list_of_all_reviews = []

for index, row in df.iterrows():
    list_of_ind_reviews = row['review'].split(", ")
    for review in list_of_ind_reviews:
        list_of_all_reviews.append(review)

# print(list_of_all_reviews)

def countOccurrence(a):
  k = {}
  for j in a:
    if j in k:
      k[j] +=1
    else:
      k[j] =1
  return k

sorted_count = dict( sorted(countOccurrence(list_of_all_reviews).items(), key=operator.itemgetter(1),reverse=True))
dict_items = sorted_count.items()
top_10_char_list = list(dict_items)[:10]

# print(top_10_char_list)

# create correct dictionary format
gs_dict = []
for review in top_10_char_list:
    gs_dict.append({
        "characteristic": review[0],
        "count": review[1]
    })

print(gs_dict)

# create and write new data to a new csv file
headers = ['characteristic', 'count']
with open('characteristic_count.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = headers)
    writer.writeheader()
    writer.writerows(gs_dict)
