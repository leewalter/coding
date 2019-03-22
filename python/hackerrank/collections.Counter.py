'''
https://www.hackerrank.com/challenges/collections-counter/problem
'''
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':

    shoes_count = int(input())
    shoes1 = map(int, input().rstrip().split()) # rem to convert from string to int for later matching in c.get
    order_count = int(input())
    c = Counter(shoes1)
    #print(c)
    total = 0

    for i in range(order_count):
        order, price = (map(int, input().rstrip().split()))
        #print(order,price)
        #print(c.get(order), 0)

        if c.get(order, 0) != 0 : # has this size in inventory 
            total += price # tally up the total 
            c[order] -= 1 # reduce inventory of this size by 1 


    print (total)
    
'''
test case:

inputs:

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

output:
200
'''
