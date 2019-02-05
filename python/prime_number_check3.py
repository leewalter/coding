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
    if (check_prime(i)):
        prime_list.append(i)

print(prime_list)

'''
-1 is not a prime no
0 is not a prime no
1 is not a prime no
2 is a prime no
3 is a prime no !
4 is not a prime no because divisible by 2
5 is a prime no !
6 is not a prime no because divisible by 2
7 is a prime no !
8 is not a prime no because divisible by 2
9 is not a prime no because divisible by 3
10 is not a prime no because divisible by 2
11 is a prime no !
12 is not a prime no because divisible by 2
13 is a prime no !
14 is not a prime no because divisible by 2
15 is not a prime no because divisible by 3
16 is not a prime no because divisible by 2
17 is a prime no !
18 is not a prime no because divisible by 2
19 is a prime no !
20 is not a prime no because divisible by 2
21 is not a prime no because divisible by 3
22 is not a prime no because divisible by 2
23 is a prime no !
24 is not a prime no because divisible by 2
25 is not a prime no because divisible by 5
26 is not a prime no because divisible by 2
27 is not a prime no because divisible by 3
28 is not a prime no because divisible by 2
29 is a prime no !
30 is not a prime no because divisible by 2
31 is a prime no !
32 is not a prime no because divisible by 2
33 is not a prime no because divisible by 3
34 is not a prime no because divisible by 2
35 is not a prime no because divisible by 5
36 is not a prime no because divisible by 2
37 is a prime no !
38 is not a prime no because divisible by 2
39 is not a prime no because divisible by 3
40 is not a prime no because divisible by 2
41 is a prime no !
42 is not a prime no because divisible by 2
43 is a prime no !
44 is not a prime no because divisible by 2
45 is not a prime no because divisible by 3
46 is not a prime no because divisible by 2
47 is a prime no !
48 is not a prime no because divisible by 2
49 is not a prime no because divisible by 7
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

'''
