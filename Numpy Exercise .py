#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises 
# 
# 

# #### Import NumPy as np

# In[1]:


import numpy as np


# #### Create an array of 10 zeros 

# In[2]:


zero_array = np.zeros(10)
zero_array


# #### Create an array of 10 ones

# In[4]:


ones_array = np.ones(10)
ones_array


# #### Create an array of 10 fives

# In[6]:


fives_array = ones_array * 5
fives_array


# #### Create an array of the integers from 10 to 50

# In[8]:


np.arange(10,51)


# #### Create an array of all the even integers from 10 to 50

# In[9]:


np.arange(10,51,2)


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[10]:


np.arange(0,9,1).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[14]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[19]:


np.random.rand(2)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[20]:


np.random.randn(25)


# #### Create the following matrix:

# In[25]:


np.linspace(.01,1,100).reshape(10,10)


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[26]:


np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[28]:


arr = np.arange(1,26,1).reshape(5,5)
arr


# In[39]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[29]:


arr[2:,1:]


# In[29]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[31]:


arr[3:4,4]


# In[30]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[32]:


arr[0:3,1:2]


# In[31]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[34]:


arr[4:5,:]


# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[35]:


arr[3:5,:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[36]:


arr.sum()


# #### Get the standard deviation of the values in mat

# In[38]:


arr.std()


# #### Get the sum of all the columns in mat

# In[39]:


arr.sum(axis=0)


# In[ ]:




