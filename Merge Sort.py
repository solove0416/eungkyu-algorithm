#!/usr/bin/env python
# coding: utf-8

# In[10]:


import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2  
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    
    return sorted_list

def timed_merge_sort(arr):
    start_time = time.time()  
    sorted_arr = merge_sort(arr)
    end_time = time.time()    
    elapsed_time = end_time - start_time
    return sorted_arr, elapsed_time


arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, elapsed_time = timed_merge_sort(arr)

print(f"정렬된 배열: {sorted_arr}")
print(f"합병 정렬 수행 시간: {elapsed_time:.6f} 초")

