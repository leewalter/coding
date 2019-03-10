'''
https://www.hackerrank.com/challenges/time-conversion/submissions/code/101452902

12 hr --> 24 hr 
use time object for simple conversion, otherwise a lot of code to change !

see complex code example at 
https://www.geeksforgeeks.org/python-program-convert-time-12-hour-24-hour-format/
# Python program to convert time 
# from 12 hour to 24 hour format 
  
# Function to convert the date format 
def convert24(str1): 
      
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if str1[-2:] == "AM" and str1[:2] == "12": 
        return "00" + str1[2:-2] 
          
    # remove the AM     
    elif str1[-2:] == "AM": 
        return str1[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif str1[-2:] == "PM" and str1[:2] == "12": 
        return str1[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(str1[:2]) + 12) + str1[2:8] 
  
# Driver Code         
print(convert24("08:05:45 PM")) 

'''

#!/bin/python3

import os
import sys
from datetime import * 

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    #format string into time object , then convert to 24 hour format
    in_time = datetime.strptime(s, "%I:%M:%S%p")
    out_time =  datetime.strftime(in_time, "%H:%M:%S")
    print(out_time)


if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    #f.write(result + '\n')

    #f.close()
	
'''
test1:
Input (stdin)Download
07:05:45PM
Your Output (stdout)
19:05:45
Expected OutputDownload
19:05:45

test2:
Input (stdin)
12:05:45PM
Your Output (stdout)
12:05:45

test3:  **note how to change 12AM to 00 hr! **
Input (stdin)
12:05:45AM
Your Output (stdout)
00:05:45

'''	