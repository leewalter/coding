'''
https://www.hackerrank.com/challenges/the-birthday-bar/submissions/code/102134070

Function Description

Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

birthday has the following parameter(s):

s: an array of integers, the numbers on each of the squares of chocolate
d: an integer, Ron's birth day
m: an integer, Ron's birth month

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    method_count = 0

    for i in range(len(s)):
        if sum_m(s,i,m,d):
            method_count += 1
    print(method_count)
    return(method_count)

def sum_m(s,i,m,d):  # can simplify with one function only later
    temp_sum = 0
    if len(s) - i >= m : # calc sum
        for k in range(i,i+m):
            temp_sum += s[k]
        if temp_sum == d:
            return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
    input1 = "5"
    input2 = "1 2 1 3 2"
    input3 = "3 2"

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input1.strip())

    s = list(map(int, input2.rstrip().split()))

    dm = input3.rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
'''
