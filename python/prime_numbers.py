# find prime numbers based on https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19

primes = []
candidates = list(range(2, 21))  # find prime numbers from 2 to 21; 1 is not a prime number
#print("candidates list is:", candidates)

while len(candidates) > 0:
    #print("length is: ", len(candidates))
    prime = candidates[0] # 2 is the first prime number
    #print("prime is", prime)
    primes.append(prime)
    #print("primes list is : ", primes)
    candidates = candidates[1:] # start checking from 3
    #    print("candidates list is:" , candidates)
    #    print("candidates[1:] list is:" , candidates[1:])
    for x in candidates[:]:
        #print("candidates list is:", candidates)
        #print("x is: ", x)
        if (x % prime) == 0:  # check if x in candidates list is divisible by prime numbers, e.g. 2,3,5 in the prime list
            #print("removing ", x)
            candidates.remove(x) # remove those divisible by 2,3,5,7 ,etc. to reduce candidates list

print("final prime numbers list", primes)

'''
final prime numbers list [2, 3, 5, 7, 11, 13, 17, 19]

'''
