# https://www.hackerrank.com/challenges/staircase/copy-from/101430354
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    string = ""
    for i in range(1,n+1):
        string = ""
        for j in range(n):
            if i + j >= n:
                string += "#"
            else:
                string += " "    
        print(string)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
	
'''
Sample Input

6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
Explanation

The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .

D:\Python\Python37-32\python.exe C:/Users/cheer/.PyCharmCE2018.2/config/scratches/scratch_31.py
10
         #
        ##
       ###
      ####
     #####
    ######
   #######
  ########
 #########
##########

'''	