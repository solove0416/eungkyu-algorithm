#!/usr/bin/env python
# coding: utf-8

# In[4]:


def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"이동: {from_rod} -> {to_rod}")
    else:
        hanoi(n - 1, from_rod, aux_rod, to_rod)
        print(f"이동: {from_rod} -> {to_rod}")
        hanoi(n - 1, aux_rod, to_rod, from_rod)


n = 3  
hanoi(n, 'A', 'C', 'B')  

