#!/usr/bin/env python
# coding: utf-8
# after you get all the data you need, you can easily combine different datasets using this code
# In[1]:


import os
import pandas as pd
import glob

files = glob.glob(r'/Users/Desktop/data/*.csv')   #folder which contains all the csv files

df = pd.concat([pd.read_csv(f, index_col=[0,1])for f in files])

df.to_csv(r'\data.csv')


# In[ ]:




