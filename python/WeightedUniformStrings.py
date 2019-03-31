'''
https://www.hackerrank.com/challenges/weighted-uniform-string/submissions/code/103566951

'''
#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):


#based on fast set and dictionary - calc the dictionary of unique scores in string
#then loop queries to check if any in the set

    list1 = list(string.ascii_lowercase) # list comprehension for a-z
    list2 = [k for k in range(1,27)]
    dict1 = dict(zip(list1,list2)) # for the a:z dict for 1:26
    len1 = len(s)
    scores = set() # store the string set of values based on uniform substrings defination above
    ctr = 1
    for i in range(len1):
        score = dict1[s[i]]    # form uniq set of values per char in string
        ctr = ctr+1 if (i+1 !=len1 and s[i+1] == s[i]) else 1 # check if consecutive char 
        scores.add(score*ctr) # ctr = 1 if single char, = 2,3,4 * score if consecutive

    result = []
    for j in queries:
        #print("Yes" if j in scores else "No") # print Yes if such in set = scores 
        result.append("Yes" if j in scores else "No")
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
