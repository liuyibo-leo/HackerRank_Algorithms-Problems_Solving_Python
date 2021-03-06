#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    
    if ar_count > 0 and [ar[i] <= 1000 for i in range(len(ar))]:
        sumOutput = 0
        for i in range(len(ar)):
            # if ar[i] <=1000:
            sumOutput += ar[i]
        return sumOutput
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

###########################################
# for my own practice
    
n = 6
ar = [1, 2, 3, 4, 10, 11]
 

def simpleArraySum(ar):
    # Write your code here
    
    if n > 0 and [ar[i] <= 1000 for i in range(len(ar))]:
        sumOutput = 0
        for i in range(len(ar)):
            # if ar[i] <=1000:
            sumOutput += ar[i]
        return sumOutput
     
    
print(simpleArraySum(ar))
