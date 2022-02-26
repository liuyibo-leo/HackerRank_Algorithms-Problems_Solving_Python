#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    length = len(arr)
    arr.sort(reverse = False)
    arr2 = arr
    a = sum(arr2[:length - 1])
    b = sum(arr2[-(length -1):])
    return print(a, b)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

   ###############
  #for my own practice
  arr = [1, 2, 3, 4, 5]

# method 1
def miniMaxSum1(arr):
    # Write your code here
    length = len(arr)
    arr.sort(reverse = False)
    arr2 = arr
    a = sum(arr2[:length - 1])
    b = sum(arr2[-(length -1):])
    print(a, b)

# method 2
def miniMaxSum2(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print ( sum-max(arr), sum-min(arr))
    
# method 3
def miniMaxSum3(arr):
    # Write your code here
    Sum = sum(arr)
    a = Sum - max(arr)
    b = Sum - min(arr)
    print(a, b)

print(miniMaxSum1(arr))
print(miniMaxSum2(arr))
print(miniMaxSum3(arr))
