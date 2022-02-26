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
    if 1<= candles_count <= 10^5 and [1<= i <= 10^7 for i in candles]:
        Max = max(candles)
        counts = candles.count(Max)
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
