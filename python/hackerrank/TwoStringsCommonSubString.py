# https://www.hackerrank.com/challenges/two-strings/problem
'''
Given two strings, determine if they share a common substring. A substring may be as small as one character.

For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    '''
    :param s1: input string 1
    :param s2: input string 2
    :return: "YES" or "NO"
    check only 1 char matching or not, if at least 1 char matching, then return YES
    '''

    result = "NO" # default is NO, change to YES only find a single char matching

    if len(s1) > len (s2) :
        s1, s2 = s2, s1 # use smallest string to check against

    for i in range(len(s1)):
        if s1[i] not in s2:
            continue
        else:
            return "YES"
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

