#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    counts = 0
    Max = max(candles)
    for i in range(len(candles)):
        if (candles[i] == Max):
            counts = counts + 1
    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


    
############
#for my own practice
candles_count = 4
candles = [3, 2, 1, 3]



def birthdayCakeCandles(candles):
    # Write your code here
    if 1<= candles_count <= 10^5 and [1<= i <= 10^7 for i in candles]:
        Max = max(candles)
        counts = candles.count(Max)
        return counts

print(birthdayCakeCandles(candles))

#method 2
def birthdayCakeCandles(candles):
    # Write your code here
    counts = 0
    Max = max(candles)
    if 1<= candles_count <= 10^5 and [1<= i <= 10^7 for i in candles]:
        for i in candles:
            if i == Max:
                counts = counts + 1
        return counts
    
 #method 3
def birthdayCakeCandles(candles):
    # Write your code here
    counts = 0
    Max = max(candles)
    if 1<= candles_count <= 10^5 and [1<= i <= 10^7 for i in candles]:
        for i in range(len(candles)):
            if candles[i] == Max:
                counts = counts + 1
        return counts


#final answer:
candles_count = 4
candles = [3, 2, 1, 3]



def birthdayCakeCandles(candles):
    # Write your code here
    counts = 0
    Max = max(candles)
    for i in range(len(candles)):
        if (candles[i] == Max):
            counts = counts + 1
    return counts
        

print(birthdayCakeCandles(candles))
