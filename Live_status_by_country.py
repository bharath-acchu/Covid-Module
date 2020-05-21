#!/usr/bin/env python
# coding: utf-8

# In[11]:


import time

from covid import Covid

covid = Covid()

country = input("\nEnter country name  :")

data = covid.get_status_by_country_name(country.lower())
print(data)
time.sleep(5)


# In[ ]:




