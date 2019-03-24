'''
https://www.hackerrank.com/challenges/extra-long-factorials/submissions/code/102918318

good to use mid-point breaking to make it smaller multiplication
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n < 2:
       return 1
    return range_prod(1,n)  

def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

  

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
