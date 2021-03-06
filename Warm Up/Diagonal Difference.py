#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    a = 0
    b = 0
    
    for i, l, j in zip(range(len(arr)), range(len(arr)), range(len(arr) - 1, -1, -1)):
        if -100 <= arr[i][i] <= 100:
            a = a + arr[i][i]
            b = b + arr[l][j]
            
    c = abs(a - b)
    return c  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

########################
#for my own practice

n = 3
arr = [[11, 2, 4],
       [4, 5, 6],
       [10, 8, -12]]

def diagonalDifference(arr):
    # Write your code here
    a = 0
    b = 0
    
    for i, l, j in zip(range(len(arr)), range(len(arr)), range(len(arr) - 1, -1, -1)):
        if -100 <= arr[i][i] <= 100:
            a = a + arr[i][i]
            b = b + arr[l][j]
            print(a, 'a')
            print(b, 'b')
    c = abs(a - b)
    return c


print(diagonalDifference(arr))
