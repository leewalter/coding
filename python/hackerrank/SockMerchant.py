'''
https://www.hackerrank.com/challenges/sock-merchant/problem

'''
#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    c = collections.Counter(ar)
    print(c)
    total = 0
    for item, count in c.most_common():
        #print(item, count)
        pair, left = divmod(count, 2)
        total += pair
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
test1:
    input1 = "9"
    input2 = "10 20 20 10 10 30 50 10 20"
    n = int(input1)
    ar = list(map(int, input2.rstrip().split()))
'''    
