
# coding: utf-8

# ## access with criteria
# -  condition based approch to get columns and rows
# -  group by function

# In[2]:


import pandas as pd
import numpy as np


# In[5]:


path='D:/Datasets/DiabaticData/diabetes.csv'
data=pd.read_csv(path)
data.head()


# ## access the columns with condition or criteria
# 

# In[6]:


data1=data[data.Age>70]
data1


# In[13]:


data2=data[(data.Age>50) & (data.Age<=80)]
data2


# In[11]:


# max value in column
data1[data1.Age==data1.Age.max()]


# ## multiple criteria or condition
# 

# In[15]:


data2=data[(data.Outcome==0) & (data.Glucose>100)]
data2


# In[20]:


Age_21=data[data.Age==21]
Age_21.count()


# ## Pandas groupBy  

# In[16]:


gp=data.groupby("Age")
gp.sum()


# In[25]:


gp1=data2[data2.Age==24]
gp1


# In[24]:


coln=data.iloc[:4,:3]
coln

