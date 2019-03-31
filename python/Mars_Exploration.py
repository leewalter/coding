'''
https://www.hackerrank.com/challenges/mars-exploration/submissions/code/103539989

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    n , r = divmod(len(s), 3)  # n = 3 if len(s) = 9
    #print(n,r)  
    count = 0
    for i in range(n):
        # check 3 char at a time:
        start = int(i*3)
        end = int(i*3+3)
        #print(start,end)
        if s[start:end] != "SOS":
            # need to count each char of the 3 to get total count of mismatch:
                if s[start] != "S":
                    count += 1
                if s[start+1] != "O":
                    count +=1
                if s[start+2] != "S":
                    count += 1

    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
