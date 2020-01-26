# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:00:00 2020

@author: Dennis O.
"""

# load pandas library
import pandas as pd


# load and read  the dataset from working directory
ndata = pd.read_csv('netflix_titles_nov_2019.csv')

# Show Dataframe
size = ndata.shape
ndata.columns
ndata.describe()

# remove duplicates
ndata.drop_duplicates(inplace = True)

# check for any null values and % of the null values 
ndata.isnull().any()
ndata.isnull().sum()/size[0]
  
# remove null columns and rows over a threhold
thresh = len(ndata)*.8
ndata.dropna(thresh=thresh, axis = 1).shape
ndata.dropna(thresh=10, axis = 0).shape

# convert text to all lower or upper
ndata.description.head()
ndata.description.head().apply(lambda x: x.lower())


#################### visualizations  #############################
ndata.boxplot('release_year')

ndata.hist('release_year')

# End of Script