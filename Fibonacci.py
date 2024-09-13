#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibonacci(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)

num = 10
result = fibonacci(num)
print(result)

