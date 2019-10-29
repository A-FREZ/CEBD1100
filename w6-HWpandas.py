# Lecture 6: Pandas
# Homework: Write a program that prints the listings in `complete.csv`
#  with a price ranging from $100 to $150 (included).

import numpy
import matplotlib
import pandas as pd #Note that from now on 'pd' replaces 'pandas'
df = pd.read_csv("data/complete.csv")
'''
print('')
print('(df["price"] > 100) & (df["price"] < 150))  #True if 100<price<150'
print((df["price"] > 100) & (df["price"] < 150))
'''
print('')
print('df.query("price >= 100 and price <= 150"):  Rows with 100 <= price <= 150 ')
print(df.query("price >= 100 and price <= 150"))

