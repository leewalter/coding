'''
https://www.hackerrank.com/challenges/hackerrank-in-a-string/submissions/code/103544190
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
''' try simple in discussion below'''

def hackerrankInString(s):
    # Complete this function
    p = 0
    for e in 'hackerrank':
        if e in s[p:]:  # very smart to move p forward in s
            p = s.index(e,p) + 1 
        else:
            return 'NO'
    return 'YES'


'''
missed two of test cases - e.g. test1 with 100 test strings - may took too long in below algo


def hackerrankInString(s):
    # need 2x'a' , 1x'c', 1x'e', 1x'h', 2x'k', 1x'n', 2x'r'
    # will test with find and rfind (last index) to see if =2

    for i in "hackerrank":
        if find_index(i, s) == -1  :
            return "NO"
        elif (i == "a" or i == "k" or i == "r") and find_index(i,s) < 2 :
            return "NO"
    return "YES"

def find_index(a,s):
    # a is char ; s= string
    first = s.find(a)
    last = s.rfind(a)
    result = 0
    if first < 0 or first == None : # -1 or None means  not found
        result = -1
    elif first > 0 and last < 0: # only 1 char
        result = 1
    elif first > 0 and last > 0: # at least 2 char
        result = 2
    return result
'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
