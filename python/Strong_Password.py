'''
https://www.hackerrank.com/challenges/strong-password/submissions/code/103472161
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

 
#    try the one in discussion instead
#    very concise with any () below 


    count = 0    
    if any(i.isdigit() for i in password)==False:
        count+=1
    if any(i.islower() for i in password)==False:
        count+=1
    if any(i.isupper() for i in password)==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password)==False:
        count+=1
    return max(count,6-n)

''' wrong below because matching ALL in substring, just need to match 1 inside substring!    
    count =  [0 for i in range(5)]
    temp = 0 
    n = len(password)
    if n < 6:
        count[0] = 6 - n
    elif   password.find("0123456789") == -1:
        count[1] = 1
    elif password.find("abcdefghijklmnopqrstuvwxyz") == -1:
        count[2] = 1
    elif password.find("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == -1:
        count[3] = 1      
    elif password.find("!@#$%^&*()-+") == -1:
        count[4] = 1

    for i in range(1,5):
        temp += count[i]

    if temp > max(count):
        return temp
    else:    
        return max(count)
'''




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
