'''
https://www.hackerrank.com/challenges/bon-appetit/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, n, k, b):
    sum = 0
    for i in range(n):
        if i != k :
            sum += bill[i]
    anna_share = int(sum/2)
    if b == anna_share:
        print("Bon Appetit")
    else:
        print(b-anna_share)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, n, k, b)
