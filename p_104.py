# -*- coding: utf-8 -*-
"""P-104.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1skypWn0HYX1nolayz3LZL_71bHx_sYLe
"""

from google.colab import files
data_to_load = files.upload()

import csv
with open("height-weight12.csv",newline = "") as f:
  reader = csv.reader(f)
  file_data = list(reader)
file_data.pop(0)
print(file_data)

new_data = []
for i in range(len(file_data)):
  n_num = file_data[i][1]
  new_data.append(float(n_num))


n = len(new_data)
total = 0
for x in new_data:
  total += x

mean = total/n
print("mean/average is :"+ str(mean))

from google.colab import files
data_to_load = files.upload()

import csv
with open("SOCR-HeightWeight.csv",newline = "") as f:
  reader = csv.reader(f)
  file_data = list(reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
  n_num = file_data[i][1]
  new_data.append(float(n_num))


n = len(new_data)
total = 0
for x in new_data:
  total += x

mean = total/n
print("mean/average is :"+ str(mean))

new_data = []
for i in range(len(file_data)):
  n_num = file_data[i][1]
  new_data.append(n_num)

n = len(new_data)
new_data.sort()
if n%2 == 0 :
  median1 = float(new_data[n//2])
  median2 = float(new_data[n//2 -1])
  median = (median1 +median2)/2

else:
  median = new_data[n//2]

print("median is : "+str(median))