#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    if 1 <= ar_count <= 10 and [0 <= ar[i] <= 10^10 for i in range(len(ar))]:
        SumResult = 0
        for i in range(len(ar)):
            SumResult = SumResult + ar[i]
        return SumResult
      
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
  
  ##########################################
  #for my own practice
  
ar_count = 5
ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]


def aVeryBigSum(ar):
    # Write your code here
    if 1 <= ar_count <= 10 and [0 <= ar[i] <= 10^10 for i in range(len(ar))]:
        SumResult = 0
        for i in range(len(ar)):
            SumResult = SumResult + ar[i]
        return SumResult
    
print(aVeryBigSum(ar))
