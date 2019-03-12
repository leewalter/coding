#https://www.hackerrank.com/challenges/migratory-birds/submissions/code/101656701

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    type1 = 0
    count1 = 0
    # use collections.Counter and most_common(5) 
    c= collections.Counter(arr)
    for type, count in c.most_common(5):
        print(type, count)
        if count1 == 0: 
            # save 1st 
            type1 = type
            count1 = count

        elif count > count1 : 
            count1 = count
            type1 = type
        elif count == count1:
            # check which type smaller
            if type1 > type:
                type1 = type        
            
    return (type1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
