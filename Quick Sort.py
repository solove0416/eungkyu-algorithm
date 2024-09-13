#!/usr/bin/env python
# coding: utf-8

# In[7]:


import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def timed_quick_sort(arr):
    start_time = time.time()  
    sorted_arr = quick_sort(arr)
    end_time = time.time()    
    elapsed_time = end_time - start_time
    return sorted_arr, elapsed_time


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr, elapsed_time = timed_quick_sort(arr)

print(f"Quick 배열: {sorted_arr}")
print(f"수행 시간: {elapsed_time:.6f} 초")

