# https://www.hackerrank.com/challenges/mini-max-sum/submissions/code/101450417

'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

For example, . Our minimum sum is  and our maximum sum is . We would print

Explanation

Our initial numbers are , , , , and . We can calculate the following sums using four of the five integers:

If we sum everything except , our sum is .
If we sum everything except , our sum is .
If we sum everything except , our sum is .
If we sum everything except , our sum is .
If we sum everything except , our sum is .
Hints: Beware of integer overflow! Use 64-bit Integer.

*** I sort and then use lambda and reduce for quick sums !
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import functools 

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
# I sort and then use lambda and reduce for quick sums !
    arr.sort() # sort from smallest to largest 

    arr1 = arr[:-1] # extrace from 0 to 2nd last elements
    min1 = functools.reduce(lambda x,y: x+y, arr1) # sum them up

    arr2 = arr[1:] # extract from 1st to last elements
    max1 = functools.reduce(lambda x,y: x+y, arr2) #sum them up 

    print (min1,max1)
    return min1, max1


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    #print(arr)
    miniMaxSum(arr)
	
'''
Input (stdin)Download
1 2 3 4 5
Your Output (stdout)
10 14
Expected OutputDownload
10 14
'''	