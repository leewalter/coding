def foobar(n):
    if (n == 0):  # for special case if zero, then will print out foobar because 0 % 3|5 = 0 
        print("0 is not multiple of 3 and/or 5 %d", n)
    else:
        if ( n % 3 == 0 and n % 5 ==0 ): # multiples of both 3 and 5
            print("foobar")
        elif ( n % 3 == 0):
            print("foo")
        elif ( n % 5 == 0 ):
            print("bar")
        else:  # not any multiple , print itself
            print(n, " is not multiple of 3 and/or 5 ")


for i in range(31):
    #print(i)
    foobar(i)
    
'''
0 is not multiple of 3 and/or 5 %d 0
1  is not multiple of 3 and/or 5 
2  is not multiple of 3 and/or 5 
foo
4  is not multiple of 3 and/or 5 
bar
foo
7  is not multiple of 3 and/or 5 
8  is not multiple of 3 and/or 5 
foo
bar
11  is not multiple of 3 and/or 5 
foo
13  is not multiple of 3 and/or 5 
14  is not multiple of 3 and/or 5 
foobar
16  is not multiple of 3 and/or 5 
17  is not multiple of 3 and/or 5 
foo
19  is not multiple of 3 and/or 5 
bar
foo
22  is not multiple of 3 and/or 5 
23  is not multiple of 3 and/or 5 
foo
bar
26  is not multiple of 3 and/or 5 
foo
28  is not multiple of 3 and/or 5 
29  is not multiple of 3 and/or 5 
foobar
'''
