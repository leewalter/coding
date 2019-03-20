'''

https://www.hackerrank.com/snippets/fde7efcb-163f-4574-a896-4944d37edb3e/quietwalters-snippet-from-alternating-characters

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count_delete = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count_delete += 1
    return count_delete

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
