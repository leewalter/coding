'''
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
Function Description

Complete the breakingRecords function in the editor below. It must return an integer array containing the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.

breakingRecords has the following parameter(s):

scores: an array of integers
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min1 = 0
    max1 = 0
    countermin1 = 0
    countermax1 = 0

    for i in range(len(scores)):
        if i == 0:  # init min1 and max1 = first element in scores
            min1 = scores[i]
            max1 = scores[i]
        else:
            if scores[i] < min1:
                min1 = scores[i]
                countermin1 += 1
            elif scores[i] > max1:
                max1 = scores[i]
                countermax1 += 1
    print(countermax1, countermin1)
    return(countermax1, countermin1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
