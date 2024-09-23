#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import math
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

def find_closest_pair(points):
    min_dist = float('inf')
    pair = (None, None)

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

def main():
    num_points = int(input("Enter the number of points: "))
    points = [Point(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_points)]
    
    start_time = time.time()
    pair, min_dist = find_closest_pair(points)
    elapsed_time = time.time() - start_time

    if pair[0] and pair[1]:
        print(f"Closest Pair: ({pair[0].x:.2f}, {pair[0].y:.2f}) and ({pair[1].x:.2f}, {pair[1].y:.2f})")
        print(f"Distance: {min_dist:.2f}")
    else:
        print("No points available.")
    
    print(f"Time taken: {elapsed_time:.6f} seconds")

if __name__ == "__main__":
    main()

