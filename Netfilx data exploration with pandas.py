# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:09:24 2020

@author: Dennis O.
"""
# 
# importing pandas library 
import pandas as pd

# importing the Netflix November 2019 dataset from Kaggle
ndata= pd.read_csv('netflix_titles_nov_2019.csv')

# determine the data size
ndata.shape

# the first five rows of the dataset

ndata.head()

# the last five rows of the dataset
ndata.tail()

# showing the columns
ndata.columns

# see more information about the dataset
ndata.info()

# describe the dataset
ndata.describe()

# the types of the data 
ndata.dtypes

# showing null values
ndata.isnull().any()

# showing the total numbers of null values for each columns
ndata.isnull().sum()

# the size percentage of the null values
ndata.isnull().sum() / ndata.shape[0]

# type of Netfilx listing
ndata.type

# type of Netflix 
ndata.type.unique()

# number counts between movies and shows
ndata.type.value_counts()

# the count percentage
ndata.type.value_counts()/ ndata.type.notnull().sum()

########################## graphs ################################

# Histogram  for release year
ndata.release_year.plot(kind ='hist')

# Histogram  for release year in bins size of 50
ndata.release_year.hist(bins = 50)

# Bar Chart for the data type count
ndata.type.value_counts().plot(kind = 'bar')

# End of script