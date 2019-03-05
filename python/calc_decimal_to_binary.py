'''
recursive to calc decimal to binay
'''

def calc(n):
    if n == 0:
        return 0
    else:
        return(int(n%2)+10*calc(int(n/2)))

for i in range(1,11):
    print(calc(i))

'''
1
10
11
100
101
110
111
1000
1001
1010
'''
   
