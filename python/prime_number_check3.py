# simple python to find out the list of prime numbers

def check_prime(n):
    if ( n < 2 ):
        print ("%d is not a prime no"  %n)
        return 0
    elif (n == 2):
        print ("%d is a prime no"  %n)
        return 1
    for x in range(2,n):
        #print(x)
        if (n % x == 0):
            print("%d is not a prime no because divisible by %d" %(n, x))
            return 0
    print ("%d is a prime no !" %n)
    return 1

prime_list = []
for i in range(-1,50):
    if i % 2 == 1 or i ==2 :
        if (check_prime(i)):
            prime_list.append(i)

print(prime_list)

'''
-1 is not a prime no
1 is not a prime no
2 is a prime no
3 is a prime no !
5 is a prime no !
7 is a prime no !
9 is not a prime no because divisible by 3
11 is a prime no !
13 is a prime no !
15 is not a prime no because divisible by 3
17 is a prime no !
19 is a prime no !
21 is not a prime no because divisible by 3
23 is a prime no !
25 is not a prime no because divisible by 5
27 is not a prime no because divisible by 3
29 is a prime no !
31 is a prime no !
33 is not a prime no because divisible by 3
35 is not a prime no because divisible by 5
37 is a prime no !
39 is not a prime no because divisible by 3
41 is a prime no !
43 is a prime no !
45 is not a prime no because divisible by 3
47 is a prime no !
49 is not a prime no because divisible by 7
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

'''
