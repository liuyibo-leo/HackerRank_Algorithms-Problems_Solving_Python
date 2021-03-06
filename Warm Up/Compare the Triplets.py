#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    if [1 <= a[i] <= 100 for i in range(len(a))] and [1 <= b[l] <= 100 for l in range(len(b)) ]:
        alice = 0
        bob = 0
        for i in range(len(a)):
            if a[i] > b[i]:
                alice = alice + 1
            elif a[i] < b[i]:
                bob = bob + 1
        return alice, bob
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
    
  
  # For my own practice
  
a = [1, 2, 3]
b = [3, 2, 1]

def compareTriplets(a, b):
    # Write your code here
    if [1 <= a[i] <= 100 for i in range(len(a))] and [1 <= b[l] <= 100 for l in range(len(b))]:
        alice = 0
        bob = 0
        for i in range(len(a)):
            if a[i] > b[i]:
                alice = alice + 1
            elif a[i] < b[i]:
                bob = bob + 1
        return alice, bob
        
print(compareTriplets(a, b))
