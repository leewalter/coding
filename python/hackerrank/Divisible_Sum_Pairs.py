#https://www.hackerrank.com/challenges/divisible-sum-pairs/submissions/code/101655516

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations 

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0 
    combo = list(combinations(ar,2)) # find all combo
    for i in range(len(combo)):
        if (combo[i][0] + combo[i][1]) % k == 0 :
            count +=1
    return(count)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
