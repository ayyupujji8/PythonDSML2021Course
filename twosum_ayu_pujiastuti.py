# -*- coding: utf-8 -*-
"""twosum Ayu pujiastuti.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oOe8jMS21wbVK5VxIP_MPh28Mb876pFF

#Ayu pujiastuti leetcode twosum
"""

nums = [2,7,11,15]
 target = 9

num_set = {}
for num_index, num in enumerate(nums):
  if (target-num) in num_set:
    print([num_set[target-num], num_index])
  num_set[num] = num_index