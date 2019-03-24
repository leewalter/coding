'''
https://www.hackerrank.com/challenges/sherlock-and-squares/submissions/code/102921740
timeouts in some large test cases at hackerrank, e.g.100000 with very large integer range

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0
    for i in range(a,b+1):
        i_sqrt = math.sqrt(i)
        if  i_sqrt.is_integer() :  # if integer, then a perfect square 
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
