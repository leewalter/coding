'''
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
Function Description

Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .

checkMagazine has the following parameters:

magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note
'''

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter  # use Counter to simplify 

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # return Yes or No

    dict_magazine = Counter(magazine)
    dict_note = Counter(note)
    #print(dict_magazine)
    #print(dict_note)

    for key, value in dict_note.items():
        if dict_magazine.get(key, 0) == 0 : # means not found in magazine, then return No
            return "No"
        elif dict_magazine.get(key, 0) < value : # means not enough words in magazine
            return "No"
        else: # = or > , so ok, check next word 
            continue
    return "Yes"


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    if m < n : # not enough words,so must return No
        print("No")
    else: # return Yes or No
        print(checkMagazine(magazine, note))

''' test cases below: 

    m = 6
    n = 4
    mag1 = "give me one grand today night"
    note1 = "give one grand today"

    m = 7
    n = 4
    mag1 = "ive got a lovely bunch of coconuts"
    note1 = "ive got some coconuts"

    m = 6
    n = 5
    mag1 = "two times three is not four"
    note1 = "two times two is four"

        
    code without inputs:


    magazine = mag1.rstrip().split()

    note = note1.rstrip().split()

    checkMagazine(magazine, note)

'''
