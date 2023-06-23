#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


dict= {
    "Name" : ['Hardik', 'Janenie', 'Manas','Aayush'],
    "Places" : ['Canada', 'Canada', 'Russia', 'USA'],
    "Packages" : ['1B','5B','1M','0.5M']
}


# In[4]:


f=pd.DataFrame(dict)


# In[5]:


f


# In[6]:


f.to_csv("hardik.csv")


# In[7]:


f.to_csv("hardik_index_false.csv", index = False)


# In[8]:


f.head(2)


# In[9]:


f.tail(1)


# In[10]:


f.describe()


# In[11]:


hardik = pd.read_csv('hardik.csv')


# In[12]:


hardik


# In[13]:


nothing = pd.read_csv('nothing.csv')


# In[14]:


nothing


# In[15]:


f.head(67)


# In[16]:


nothing.head(75)


# In[18]:


f.place()


# In[19]:


f


# In[20]:


f.Places


# In[21]:


f.index=['I','II','III','IV']


# In[22]:


f


# In[23]:


type(f)


# In[24]:


type(f.Name)


# In[25]:


newdf = pd. DataFrame(np.random. rand (334,5), index=np.arange (334))


# In[26]:


newdf


# In[27]:


newdf.describe()


# In[28]:


newdf.dtypes


# In[29]:


newdf[3][1]='hardik'


# In[30]:


newdf.head()


# In[31]:


newdf.to_csv("newdf.csv")


# In[32]:


type(newdf)


# In[33]:


newdf.T #this is use to transpose the dataframe


# In[34]:


newdf


# In[35]:


newdf.head()


# In[36]:


newdf. drop (4, axis=1)#axis = 0 that means row, axis = 1 means column


# In[37]:


dict1 = {
    "Bank" : ["ICICI", "SBI", "AXIS", "CITY UNION BANK", "HDFC"],
} 


# In[38]:


import pandas as pd
h= pd.DataFrame(dict1)


# In[39]:


h


# In[40]:


print("hello")


# In[41]:


hello = ("This is Deepshikha Chhipa, Sister of Mr.Hardik Chhipa")
print(hello)


# In[42]:


h


# In[43]:


h


# In[44]:


import os
import pandas as pd

current_dir = os.getcwd()


filename = 'h.csv'


file_path = os.path.join(current_dir, h)

# Read the CSV file using pandas
df = pd.read_csv(h)

# Perform operations on the dataframe as needed
# ...



# In[45]:


h


# In[46]:


nothing  =  pd.read_csv("nothing.csv")


# In[47]:


nothing


# In[48]:


nothing.head(80)


# In[49]:


nothing


# In[50]:


f


# In[ ]:




