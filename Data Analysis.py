#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


# In[2]:


df = pd.read_csv("housing2.csv")


# In[13]:


df.head()


# In[4]:


df.info()


# In[10]:


df.ocean_proximity.value_counts()


# In[12]:


df.households.head()


# In[20]:


df.households.value_counts()


# In[26]:


df.households.replace('no',0,inplace=True)


# In[27]:


df.households.value_counts()


# In[32]:


df.households.astype(float)


# In[34]:


df.info()


# In[36]:


df.households.isnull().sum()


# In[39]:


df.households.fillna(0,inplace=True)


# In[40]:


df.households.isnull().sum()


# In[54]:


df.households = df.households.astype(int)


# In[55]:


df.info()


# In[57]:


df.describe()


# In[58]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt 


# In[59]:


df.hist(bins=50,figsize=(20,15))
plt.show()


# In[60]:


df.isnull().sum()


# In[67]:


df.housing_median_age.fillna(df.housing_median_age.mean(),inplace=True)
df.total_bedrooms.fillna(df.total_bedrooms.mean(),inplace=True)
df.population.fillna(df.population.mean(),inplace=True)
df.median_income.fillna(df.median_income.mean(),inplace=True)


# In[68]:


df.isnull().sum()


# In[72]:


df.drop(['gender'],axis=1,inplace=True)


# In[74]:


df.duplicated().sum()


# In[75]:


df.info()


# In[76]:


df.plot(kind="scatter",x='longitude',y='latitude',alpha=0.1)


# In[77]:


df.plot(kind="scatter",x='longitude',y='latitude',alpha=0.1,s=df.population/100,label="population",c="median_house_value",cmap=plt.get_cmap("jet"),colorbar=True)


# In[78]:


corr_matrix = df.corr()
corr_matrix


# In[80]:


corr_matrix.median_house_value.sort_values()


# In[85]:


df_info = df.describe()


# In[92]:


df_info.loc['median'] = df.median()
df_info.loc['skew'] = df.skew()
df_info.loc['kurtosis']=df.kurt()


# In[93]:


df_info


# In[91]:





# ### Multi Model Distribution 
# 

# In[94]:


plt.subplot(2,1,1)
plt.title('Median Age of house')
sns.kdeplot(df.housing_median_age,color='teal')
plt.show()
plt.subplot(2,1,2)
plt.title('Median house value')
sns.kdeplot(df.median_house_value,color='teal')
plt.show()


# ### Almost Normal Distribution  for total Rooms & population

# Total Bedroom & Householders due to cleaning data and fill NA with mean in Bedroom and Zero in householders (It isn't the perfect way for handling NA)

# In[110]:


plt.subplot(4,1,1)
plt.title("Distribution of Room numbers")
sns.kdeplot(df.total_rooms)
plt.show()
plt.subplot(4,1,2)
plt.title("Distribution of Bedroom numbers")
sns.kdeplot(df.total_bedrooms)
plt.show()


# In[109]:


plt.subplot(2,1,1)
plt.title("Distribution of population")
sns.kdeplot(df.population)
plt.show()
plt.subplot(2,1,2)
plt.title("Distribution of Householders")
sns.kdeplot(df.households)
plt.show()


# In[103]:


plt.title('Distribution of the median income')
sns.kdeplot(df.median_income)
plt.show()


# In[104]:


df.ocean_proximity.value_counts()


# In[106]:


import plotly.express as ex


# In[107]:


ex.pie(df,names='ocean_proximity',title =' Locations')


# In[ ]:




