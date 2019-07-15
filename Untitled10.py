
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import os
print(os.listdir("E:\Data science\projects\gas-prices-in-brazil"))


# In[7]:


data = pd.read_table("E:\Data science\projects\gas-prices-in-brazil/2004-2019.tsv")


# In[8]:


data.head()


# In[9]:


data.info()


# In[10]:


data.tail()


# In[11]:


data.describe()


# In[14]:


sns.heatmap(data.corr())
plt.show()


# In[15]:


plt.matshow(data.corr())
plt.colorbar()
plt.show()


# In[16]:


p = data.hist(figsize = (20,20))

