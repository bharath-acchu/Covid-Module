#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time

from covid import Covid

covid = Covid()

def covid_worldwide():
    x = 0
    while x < 1:
        
        print("Toatal active cases :{}".format(covid.get_total_active_cases()))
        time.sleep(3)
        x= x+1
        print("Total confirmed cases : {}".format(covid.get_total_confirmed_cases()))
        time.sleep(3)
        x = x+1
        print("Total recovered cases :{}".format(covid.get_total_recovered()))
        time.sleep(3)
        x = x+1
        print("Total deaths :{}".format(covid.get_total_deaths()))
        time.sleep(2)



covid_worldwide()


# In[ ]:




