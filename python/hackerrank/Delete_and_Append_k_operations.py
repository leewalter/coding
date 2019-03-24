'''
https://www.hackerrank.com/challenges/append-and-delete/submissions/code/102921181
check if EXACT k operations will append and delete a string s to t 
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    for ops_left in reversed(range(1, k + 1)): # start from the back so reversed here 
        diff_left = len(t) - len(s)  # s will be shrinked one by one, so check diff btw s and target strings
        if s == t[:len(s)] and diff_left == ops_left or len(s) == 0: # check if now the same in new s vs target t and others
            break  # break if above ok, means good
        s = s[:-1] # s is reducing 1 by 1  # remove last char from s to form new s for next loop
    if ( diff_left >=0  and diff_left <= ops_left ) :  # must have diff_left > 0 to protect some cases 
        return "Yes"
    else:
        return "No"    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
