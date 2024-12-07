# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NQ7incqqE51GiLrc6gmL3Jy6O8RqrSJK
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

time=np.array(["September","October","November","December","January","February","March","April","May","June","July","August"])
water_cost=np.array([47.89,50.86,52.51,48.1,55.39,56.03,85.07,103.49,96.23,37.05,40.30,34.75])
sewer_cost=np.array([36.09,37.67,43.37,38.11,46.88,37.23,62.66,80.2,41.51,16.72,25.79,19.44])

total_cost=np.array([])
for i in range(len(water_cost)):
    total_cost=np.append(total_cost,water_cost[i]+sewer_cost[i])
print(list(total_cost))
plt.figure(figsize=(10,5))
plt.plot(time,water_cost,'-', linewidth=2, markersize=10,label='Water')
plt.plot(time,sewer_cost,'-', linewidth=2, markersize=10,label='Sewer')
plt.plot(time,total_cost,'-', linewidth=2, markersize=10,label='Total Cost')
plt.xlabel('Months')
plt.ylabel('Price ($)')
plt.title('Water/Sewer Costs')
plt.legend()

plt.show()

