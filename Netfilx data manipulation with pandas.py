# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:39:55 2020

@author: Dennis O.
"""

# load pandas library
import pandas as pd

#load and read  the dataset from working directory 
ndata = pd.read_csv('netflix_titles_nov_2019.csv')

# show the data columns
ndata.columns

# listing the frst 100 rows of the dataset and creat a new variable as ndata2
ndata2 = ndata.head(100)

# renaming show_id column to id
ndata2.rename(index= str, columns={'show_id':'id'}, inplace = True)

# single column
ndata['title']

# row selection 
ndata[0:100]

# multiple columns
tryt = ndata[['title','release_year','type']]

# multiple columns with the first 100 indexes
tryt2 = ndata.loc[0:100, ['title','release_year','type']]

# multiple columns with the first 100 rows and first 3 columns
tryt3 = ndata.iloc[0:100, 0:3]

# dropping columns 
ndata_nodate_added = ndata.drop('date_added', axis = 1)

 # column creation
ndata['age'] = 2019 - ndata['release_year']

# recenlty new movies and shows age <=1  filtering by this criteria 
ndata_new_netflix = ndata[ndata.age <= 1]
 
ndata.loc[ndata.age <= 1, :]
 
 # dummy variables
data_dummies = pd.get_dummies(ndata[['listed_in','description','type']].head(1000))
 
# pivot tables
pd.pivot_table (ndata, index = 'release_year', columns = 'type', \
     values='age', aggfunc = 'count').sort_index (ascending=False)
     
pd.pivot_table (ndata, index = 'release_year', columns = 'type', \
     values='age', aggfunc = 'mean').sort_index (ascending=False)    

 # pivot table with plot  
pd.pivot_table (ndata, index = 'release_year', columns = 'type', \
     values='age', aggfunc = 'mean').sort_index (ascending=False).plot()

# groupby
grouped_data = ndata.groupby(['type','age'], as_index = False).mean() 

# pd.merge == sql join
df1 = ndata[['title','rating']]
df2 = ndata[['rating','age']]

df_joined = pd.merge(df1,df2, on= 'rating')

# appendning 
samp1 = ndata.sample(100, random_state= 1)
samp2 = ndata.sample(100, random_state = 2)

samp1.append(samp2)

# write to csv
ndata.head(1000).to_csv('top1000.csv')

# End of script
