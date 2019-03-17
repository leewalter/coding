'''
https://www.hackerrank.com/challenges/between-two-sets/problem

You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

For example, given the arrays  and , there are two numbers between them:  and . , ,  and  for the first value. Similarly, ,  and , .
'''

#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    a.sort()
    b.sort()
    #print(a,b )
    min1 = a[len(a)-1]
    max1 = b[0]
    counter = 0
    if min1 < max1 :
        for i in range(min1, max1+1):
            if checkset1(i,a)  and checkset2(i,b) :
                print(i)
                counter += 1
        return counter

    elif min1 == max1 :
        # only need to test min1 = max1
        if checkset1(min1,a) == True and checkset2 (min1,b) == True :
            return 1

    else: # min1 < max1
        return 0


def checkset1(n, a):
    #result = True
    for i in a:
        #print(i,n)
        if n % i != 0:
            #print("False")
            return False
    return True

def checkset2(n,b):
    #result = True
    for i in b:
        if i % n != 0:
            return False
    return True


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()

'''
test cases


    a = [2, 4]
    b = [ 16, 32, 96]

    total = getTotalX(a, b)
    print(total)
'''
