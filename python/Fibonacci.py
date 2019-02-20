# ref - https://technobeans.com/2012/04/16/5-ways-of-fibonacci-in-python/
# add lru_cache example 0

# Example 0: using LRU Cache
# https://www.youtube.com/watch?v=Qk0zUZW-U_M&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=18

from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    if type(n) != int:
        raise TypeError("n must be a positive integer, this is not an integer!")
    if n < 1:
        raise ValueError("n must be a positive integer")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

'''
for i in range(1,1001):
    print (fib(i))
'''

## Example 1: Using looping technique
print("## Example 1: Using looping technique")
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(5))

## Example 2: Using recursion
print("## Example 2: Using recursion")
def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)
print (fibR(5))

## Example 3: Using generators
print("## Example 3: Using generators")
a,b = 0,1
def fibI():
 global a,b
 while True:
  a,b = b, a+b
  yield a
f=fibI()
for i in range(0,6):
    print ("Fib no# %d  is %d" %(i, a))
    f.__next__()
# print (a)

## Example 4: Using memoization
print("Example 4: Using memoization")
def memoize(fn, arg):
 memo = {}
 if arg not in memo:
  memo[arg] = fn(arg)
  return memo[arg]
 
## fib() as written in example 1.
fibm = memoize(fib,5)
print (fibm)

## Example 5: Using memoization as decorator
print("## Example 5: Using memoization as decorator")
class Memoize:
 def __init__(self, fn):
  self.fn = fn
  self.memo = {}
 def __call__(self, arg):
  if arg not in self.memo:
   self.memo[arg] = self.fn(arg)
   return self.memo[arg]
 
@Memoize
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(5))

'''
D:\Go-workspace\walter\coding\python>python Fibonacci.py
## Example 1: Using looping technique
5
## Example 2: Using recursion
5
## Example 3: Using generators
Fib no# 0  is 0
Fib no# 1  is 1
Fib no# 2  is 1
Fib no# 3  is 2
Fib no# 4  is 3
Fib no# 5  is 5
Example 4: Using memoization
5
## Example 5: Using memoization as decorator
5
'''
