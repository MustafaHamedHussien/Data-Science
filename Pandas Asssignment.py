#!/usr/bin/env python
# coding: utf-8

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:


df = pd.read_csv("Copy of Copy of Salaries.csv")


# ** Check the head of the DataFrame. **

# In[3]:


df.head()


# ** Use the .info() method to find out how many entries there are.**

# In[4]:


df.info()


# **What is the average BasePay ?**

# In[5]:


df.BasePay.mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[6]:


df.OvertimePay.max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[7]:


df[df['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[8]:


df[df['EmployeeName']=='JOSEPH DRISCOLL'].TotalPayBenefits


# ** What is the name of highest paid person (including benefits)?**

# In[9]:


df[df.TotalPayBenefits == df.TotalPayBenefits.max()]


# ** How many unique job titles are there? **

# In[10]:


df['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[21]:


df.JobTitle.value_counts().head()


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[22]:


sum(df[df['Year']==2013]['JobTitle'].value_counts()==1)


# # Great Job!
