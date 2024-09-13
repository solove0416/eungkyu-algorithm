#!/usr/bin/env python
# coding: utf-8

# In[1]:


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

num1 = 28
num2 = 48
gcd = euclid(num1, num2)
print(f"{num1}와 {num2}의 최대공약수는 {gcd}입니다.")

