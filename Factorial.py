#!/usr/bin/env python
# coding: utf-8

# In[3]:


def factorial(f):
    if f == 1:
        return 1
    else:
        return factorial(f - 1) * f

num = 5
result = factorial(num)
print(result)


# In[ ]:




