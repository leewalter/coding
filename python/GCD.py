'''
https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers/0
GCD of two numbers
learn the Euclidean algorithm at 
https://en.wikipedia.org/wiki/Euclidean_algorithm

function gcd(a, b)
    while b ≠ 0
       t := b; 
       b := a mod b; 
       a := t; 
    return a;
'''

def gcd(num1, num2):    
    while num2:
        num1, num2 = num2, num1%num2
        #print(num1,num2)
    return num1
    
if __name__ == "__main__":
    num_cases = int(input())
    #print(num_cases)
    for case in range(num_cases):
        nums = [int(num) for num in input().split()]
        print(gcd(nums[0], nums[1]))

'''
For Input:
2
84 16
87 8
Your Output is:
4
1
'''
