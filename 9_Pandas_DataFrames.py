# -*- coding:utf-8 -*-
"""
@author:BinLu
@file:9_Pandas_DataFrames.py
@time:2017-9-1911:50
"""

"""
Numpy's ndarrays well-suited for performing math operations on one and two-dimensional arrays of
numeric values, but they fall short when it comes to dealing with heterogeneous data sets.
To store data from an external source like an excel workbook or database,
we need a data structure that can hold different data types. It is also desirable to
be able to refer to rows and columns in the data by custom labels rather than numbered indexes

Pandas Series
Before we get into DataFrames, we'll take a brief detour to explore pandas series.
Series are very similar to ndarrays: the main difference between them is that with series,
you can provide custom index labels and then operations you perform on series automatically align the data based on the labels.
To create a new series, first load the numpy and pandas libraries (pandas is preinstalled with the Anaconda Python distribution.).
"""

import numpy as np
import pandas as pd

""""""
#Define a new series by passing a collection of homogeneous data like ndarray or list,
# along with a list of associated indexes to pd.Series():
my_series = pd.Series( data = [2,3,5,4],             # Data
                       index= ['a', 'b', 'c', 'd'])  # Indexes
my_series
"""
a    2
b    3
c    5
d    4
dtype: int64
"""

#You can also create a series from a dictionary, in which case the dictionary keys act as the labels and the values act as the data:
my_dict = {"x": 2, "a": 5, "b": 4, "c": 8}
my_series2 = pd.Series(my_dict)
my_series2
"""
a    5
b    4
c    8
x    2
dtype: int64
"""

#similar to a dictionary, you can access items in a series by the labels:
my_series["a"]
#2
#Numeric indexing also works:
my_series[0]
#2

#If you take a slice of a series, you get both the values and the labels contained in the slice:
#In [6]:
my_series[1:3]
#Out[6]:
#b    3
#c    5
#dtype: int64
#As mentioned earlier, operations performed on two series align by label:
#In [7]:
my_series + my_series
#Out[7]:
#a     4
#b     6
#c    10
#d     8
#dtype: int64
#If you perform an operation with two series that have different labels, the unmatched labels will return a value of NaN (not a number.).
my_series + my_series2
#a     7
#b     7
#c    13
#d   NaN
#x   NaN
#dtype: float64

#Other than labeling, series behave much like numpy's ndarrays. A series is even a valid argument to many of the numpy array functions we covered last time:
np.mean(my_series)        # numpy array functions generally work on series
#3.5
np.dot(my_series, my_series)
#54

##### DataFrame Creation and Indexing ######
"""A DataFrame is a 2D table with labeled columns that can each hold different types of data.
DataFrames are essentially a Python implementation of the types of tables you'd see in an Excel workbook or SQL database.
DataFrames are the defacto standard data structure for working with tabular data in Python;
we'll be using them a lot throughout the remainder of this guide.
You can create a DataFrame out a variety of data sources like dictionaries,
2D numpy arrays and series using the pd.DataFrame() function. Dictionaries provide an intuitive way to create DataFrames:
when passed to pd.DataFrame() a dictionary's keys become column labels and the values become the columns themselves:"""

# Create a dictionary with some different data types as values
my_dict = {"name" : ["Joe","Bob","Frans"],
           "age" : np.array([10,15,20]),
           "weight" : (75,123,239),
           "height" : pd.Series([4.5, 5, 6.1],
            index=["Joe","Bob","Frans"]),
           "siblings" : 1,
           "gender" : "M"}
df = pd.DataFrame(my_dict)   # Convert the dict to DataFrame
df                           # Show the DataFrame
"""
	age	gender	height	name	siblings	weight
Joe	10	M	4.5	Joe	1	75
Bob	15	M	5.0	Bob	1	123
Frans	20	M	6.1	Frans	1	239
"""
"""
Notice that values in the dictionary you use to make a DataFrame can be a variety of sequence objects,
including lists, ndarrays, tuples and series. If you pass in singular values like a single number or string,
that value is duplicated for every row in the DataFrame (in this case gender is set to "M" for all records and siblings is set to 1.).
Also note that in the DataFrame above, the rows were automatically given indexes that align with the indexes
of the series we passed in for the "height" column. If we did not use a series with index labels to create our DataFrame,
it would be given numeric row index labels by default:
"""

my_dict2 = {"name": ["Joe", "Bob", "Frans"],
            "age": np.array([10, 15, 20]),
            "weight": (75, 123, 239),
            "height": [4.5, 5, 6.1],
            "siblings": 1,
            "gender": "M"}
df2 = pd.DataFrame(my_dict2)  # Convert the dict to DataFrame
df2  # Show the DataFrame
"""
age	gender	height	name	siblings	weight
0	10	M	4.5	Joe	1	75
1	15	M	5.0	Bob	1	123
2	20	M	6.1	Frans	1	239
"""
df2 = pd.DataFrame(my_dict2,
                   index=my_dict["name"])
df2
"""
age	gender	height	name	siblings	weight
Joe	10	M	4.5	Joe	1	75
Bob	15	M	5.0	Bob	1	123
Frans	20	M	6.1	Frans	1	239
"""
# Delete a column
del df2['name']
# Add a new column
df2["IQ"] = [130, 105, 115]
df2
"""
age	gender	height	siblings	weight	IQ
Joe	10	M	4.5	1	75	130
Bob	15	M	5.0	1	123	105
Frans	20	M	6.1	1	239	115
"""


#Inserting a single value into a DataFrame causes it to be all the rows?
df2["Married"] = False
df2
"""
age	gender	height	siblings	weight	IQ	Married
Joe	10	M	4.5	1	75	130	False
Bob	15	M	5.0	1	123	105	False
Frans	20	M	6.1	1	239	115	False
3 rows × 7 columns
"""
#When inserting a Series into a DataFrame, rows are matched by index. Unmatched rows will be filled with NaN:
df2["College"] = pd.Series(["Harvard"],
                           index=["Frans"])
df2
"""
age	gender	height	siblings	weight	IQ	Married	College
Joe	10	M	4.5	1	75	130	False	NaN
Bob	15	M	5.0	1	123	105	False	NaN
Frans	20	M	6.1	1	239	115	False	Harvard
3 rows × 8 columns
"""
#You can select both rows or columns by label with df.loc[row, column]:
df2.loc["Joe"]          # Select row "Joe"
"""
age            10
gender          M
height        4.5
siblings        1
weight         75
IQ            130
Married     False
College       NaN
Name: Joe, dtype: object
"""
df2.loc["Joe","IQ"]     # Select row "Joe" and column "IQ"
#130
df2.loc["Joe":"Bob" , "IQ":"College"]   # Slice by label
"""
IQ	Married	College
Joe	130	False	NaN
Bob	105	False	NaN
2 rows × 3 columns
"""
#Select rows or columns by numeric index with df.iloc[row, column]:
df2.iloc[0]          # Get row 0
"""
age            10
gender          M
height        4.5
siblings        1
weight         75
IQ            130
Married     False
College       NaN
Name: Joe, dtype: object
"""
df2.iloc[0, 5]       # Get row 0, column 5
#130
df2.iloc[0:2, 5:8]   # Slice by numeric row and column index
"""
IQ	Married	College
Joe	130	False	NaN
Bob	105	False	NaN
2 rows × 3 columns
"""
#Select rows or columns based on a mixture of both labels and numeric indexes with df.ix[row, column]:
df2.ix[0]           # Get row 0
"""
age            10
gender          M
height        4.5
siblings        1
weight         75
IQ            130
Married     False
College       NaN
Name: Joe, dtype: object
"""
df2.ix[0, "IQ"]     # Get row 0, column "IQ"
#130
df2.ix[0:2, ["age", "IQ", "weight"]]  # Slice rows and get specific columns
"""
age	IQ	weight
Joe	10	130	75
Bob	15	105	123
2 rows × 3 columns
You can also select rows by passing in a sequence boolean(True/False) values. Rows where the corresponding boolean is True are returned:
"""
boolean_index = [False, True, True]
df2[boolean_index]
"""
age	gender	height	siblings	weight	IQ	Married	College
Bob	15	M	5.0	1	123	105	False	NaN
Frans	20	M	6.1	1	239	115	False	Harvard
2 rows × 8 columns
"""
#This sort of logical True/False indexing is useful for subsetting data when combined with logical operations.
#  For example, say we wanted to get a subset of our DataFrame with all persons who are over 12 years old.
# We can do it with boolean indexing:
# Create a boolean sequence with a logical comparison
boolean_index = df2["age"] > 12
# Use the index to get the rows where age > 12
df2[boolean_index]
"""
age	gender	height	siblings	weight	IQ	Married	College
Bob	15	M	5.0	1	123	105	False	NaN
Frans	20	M	6.1	1	239	115	False	Harvard
2 rows × 8 columns
"""
You can do this sort of indexing all in one operation without assigning the boolean sequence to a variable.
In [31]:
df2[ df2["age"] > 12 ]
Out[31]:
age	gender	height	siblings	weight	IQ	Married	College
Bob	15	M	5.0	1	123	105	False	NaN
Frans	20	M	6.1	1	239	115	False	Harvard
2 rows × 8 columns


