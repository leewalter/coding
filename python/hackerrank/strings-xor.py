'''
https://www.hackerrank.com/challenges/strings-xor/submissions/code/102872134
Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
'''

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] != t[i]:
            res += '1'
        else:
            res += '0'

    return res

s = input()
t = input()
print(strings_xor(s, t))



