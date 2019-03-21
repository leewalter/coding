'''
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
array can have +ve or -ve integers inside, always 6x6
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    n = 6 # always 6x6 array
    max = -999999999999 # need this for -ve numbers inside arrays, zero will not work !
    for i in range(1,5):  # row 1-4 only
        for j in range(1,5): # columns 1-4 only
            temp =  calc1(arr,i,j)
            if temp > max:
                max = temp
    return max


def calc1(arr, i, j): # calc hour glass for position i,j
    sum1 = 0
    sum1 = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] # top row
    sum1 += arr[i][j] # middle row
    sum1 += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1] # bottom row
    return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


'''
test case 1:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

output = 19

test case 2: -ve integer
-1 -1 0 -9 -2 -2
-2 -1 -6 -8 -2 -5
-1 -1 -1 -2 -3 -4
-1 -9 -2 -4 -4 -5
-7 -3 -3 -2 -9 -9
-1 -3 -1 -2 -4 -5

output = -6
'''
