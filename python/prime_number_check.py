# ref https://www.programiz.com/python-programming/examples/prime-number
# Python program to check if the input number is prime or not

#num = 407

# take input from the user
# num = int(input("Enter a number: "))

def check_prime(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2 ,num):
            if (num % i) == 0:
                #print(num ,"is not a prime number")
                #print(i ,"times" ,num//i ,"is" ,num)
                break
        else:
            print(num ,"is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num ,"is not a prime number")

for i in range(50):
    check_prime(i)
  
'''
0 is not a prime number
1 is not a prime number
2 is a prime number
3 is a prime number
5 is a prime number
7 is a prime number
11 is a prime number
13 is a prime number
17 is a prime number
19 is a prime number
23 is a prime number
29 is a prime number
31 is a prime number
37 is a prime number
41 is a prime number
43 is a prime number
47 is a prime number

'''
