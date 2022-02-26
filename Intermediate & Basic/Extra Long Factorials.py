#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if 1<= n <= 100:
        nNew = n
        for i in range(1, n, 1):
            nNew = (n - i) * nNew
        print(nNew)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
#################
# for my own practice
n = 25

def extraLongFactorials(n):
    # Write your code here
    if 1<= n <= 100:
        nNew = n
        for i in range(1, n, 1):
            nNew = (n - i) * nNew
            print(nNew)
        return nNew
    
print(extraLongFactorials(n))
