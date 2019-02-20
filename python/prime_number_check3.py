# ref https://www.youtube.com/watch?v=2p3kwF04xcA&index=24&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-

import math
import time

def is_prime_v2(n):
    if n <= 0:
        raise ("n must be a positive integer ! ")
        return False

    if n == 1:
        return False

    elif n == 2:
        return True

    elif n % 2 == 0:
        return False

    elif n % 3 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))  # check half of the combinations
    for d in range(5, max_divisor+1, 2):    # start from 5,7, etc..
        if n % d == 0:
            return False
    return True

'''
for n in range(1,21):
    print(n, is_prime_v2(n))
'''

t0 = time.time()
for n in range(1,1000000):
    is_prime_v2(n)

t1 = time.time()
print("time required for 1000000 :", t1-t0)

#print("test raise ", is_prime_v2(-10))

'''
if use n % 2 == 0, then 
time required for 1000000 : 9.644205331802368

without above, then close timings,
time required for 1000000 : 10.904832363128662

if add % 2 and %3, then for d in range(5, max_divisor+1, 2):
then half the time !

time required for 1000000 : 5.761587858200073
'''
