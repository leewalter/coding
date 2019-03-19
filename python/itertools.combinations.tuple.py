'''
https://www.hackerrank.com/challenges/itertools-combinations/submissions/code/102350745

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s = input()
s1, n  = s.rstrip().split()
n = int(n)
s1 = sorted(s1)  # must sort this first before combinations for proper ordering

for i in range(1,n+1):
    list1 = list(combinations(s1, i))
    list1.sort()  # does not sort well alone when [('A', 'C'), ('A', 'K'), ('C', 'K'), ('H', 'A'), ('H', 'C'), ('H', 'K')]
    #print(list1)
    list1_sorted = sorted(list1, key = lambda tup: tup[0])  # sort by 1st key
    for item_tuple in list1_sorted :
        s = ""  # reset empty string 
        for item in item_tuple:
            s += str(item)  # add back all inside the tuple element
        print(s)  # print out AC, AK, etc.

''' test cases:
Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''
