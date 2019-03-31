'''
https://www.hackerrank.com/challenges/30-arrays/submissions/code/103538301
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr = reversed(arr)  # this is very good ! 
    print(*arr,sep=" ")
