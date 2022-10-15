import ast
import pandas as pd
import re
import operator
from itertools import islice
import csv

# open file for chocolate bars
df = pd.read_csv('data/chocolate_bars.csv', usecols=['num_ingredients', 'bar_name'])
print(df.head())

