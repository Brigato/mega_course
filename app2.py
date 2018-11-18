# https://www.udemy.com/the-python-mega-course/learn/v4/content
# The Python Mega Course: Build 10 Real World Applications
# Pandas
# pip install pandas
# iPython
# pip install ipython
# jupyter notebook

import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"])

df2 = pandas.DataFrame([{"Name": "John"}, {"Name": "Jack"}])
df2 = pandas.DataFrame([{"Name": "John", "Surename": "Johns"}, {"Name": "Jack"}])  # NaN value for the second dict.

print(df2)
print(type(df2))
print(dir(df2))
print(df1.mean())  # Average values
print(df2.mean())  # Average values









