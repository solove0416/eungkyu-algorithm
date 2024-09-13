#!/usr/bin/env python
# coding: utf-8

# In[9]:


import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    return arr


def timed_bubble_sort(arr):
    start_time = time.time()  
    sorted_arr = bubble_sort(arr)
    end_time = time.time()    
    elapsed_time = end_time - start_time
    return sorted_arr, elapsed_time

arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr, elapsed_time = timed_bubble_sort(arr)

print(f"Bubble 배열: {sorted_arr}")
print(f"수행 시간: {elapsed_time:.6f} 초")

