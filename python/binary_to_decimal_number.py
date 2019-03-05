# https://practice.geeksforgeeks.org/problems/binary-number-to-decimal-number/0

def calc(binary):
# binary is a string
    value = 0
    p = binary[::-1]
    for j in range(len(p)):
        if p[j] == "1":
            value = value + (2**j)
    return value        

num=int(input())

for i in range(num):
    binary = input()
    print(calc(binary))
    
'''
Example:
Input:
2
10001000
101100
Output:
136
44
'''
