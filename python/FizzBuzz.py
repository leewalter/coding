# ref https://gist.github.com/jaysonrowe/1592775

def fizzbuzz(n):
# add some () to be more readable below
    if (n % 3 == 0 and n % 5 == 0):
        return 'FizzBuzz'
    elif (n % 3 == 0):
        return 'Fizz'
    elif (n % 5 == 0):
        return 'Buzz'
    else:
        return str(n)

# fixed print() and xrange to range from original
# print ('\n'.join(fizzbuzz(n) for n in range(1, 21)))

# more readable below,
#for n in range(1, 21):
    #print (fizzbuzz(n))

# one line, but not readable; very smart to use the + below ! 
'''
i=1
while i<21:print("Fizz"*(i%3<1)+(i%5<1)*"Buzz"or i);i+=1
'''

# more readable below,
'''
i=1
while i<21:
    print("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i)
    i+=1
'''

# change the smart one-line above to a function
def fizzbuzz2(i):
    return("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i)

for n in range(1, 21):
    print(fizzbuzz2(n))



'''
D:\Go-workspace\walter\coding\python>python FizzBuzz.py
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
'''
