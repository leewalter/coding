#https://www.hackerrank.com/challenges/grading/submissions/code/101654987

#!/bin/python3

import os
import sys
import math

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # If the difference between the  and the next multiple 5 of  is less than 3, round  up to the next multiple of 5 .
    # If the value of  is less than 38 , no rounding occurs as the result will still be a failing grade.
    #

    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        else:
            (div1, remain1) = divmod(grades[i],5)
            if remain1 >=3 :
                grades[i] = (div1+1) * (5) 
                if grades[i] > 100:
                    grades[i] = 100

    return grades       

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
