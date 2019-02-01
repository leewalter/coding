# python to locate 1 in a 2D array

#below save it into a dictionary

# python to locate 1 in a 2D array

def check_zero(array1):
    d = {}
    print("array index zeros at:")
    for i in range(len(array1)):
        index = [k for k, v in enumerate(array1[i]) if v == 0]
        d[i] = index
        #print(i, index)
    #print(d)
    return(d)

array1 = [
  [1, 1, 0, 0],
  [0, 0, 1, 1],
  [0, 1, 0, 1]
]

array2 = [
  [1, 1, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 1, 0, 1]
]

print(check_zero(array1))

print(check_zero(array2))

'''
array index zeros at:
{0: [2, 3], 1: [0, 1], 2: [0, 2]}
array index zeros at:
{0: [2, 3, 4], 1: [0, 1, 4], 2: [0, 1, 3]}
'''


# below is a function
def check_zero(array1):

    print("array index zeros at:")
    for i in range(len(array1)):
        index = [k for k, v in enumerate(array1[i]) if v == 0]

        print(i, index)

    return(i,index)

array1 = [
  [1, 1, 0, 0],
  [0, 0, 1, 1],
  [0, 1, 0, 1]
]

array2 = [
  [1, 1, 0, 0, 0],
  [0, 0, 1, 1, 0],
  [0, 0, 1, 0, 1]
]

check_zero(array1)

check_zero(array2)

'''
array index zeros at:
0 [2, 3]
1 [0, 1]
2 [0, 2]
array index zeros at:
0 [2, 3, 4]
1 [0, 1, 4]
2 [0, 1, 3]
'''




array1 = [
  [1, 1, 0, 0],
  [0, 0, 1, 1],
  [0, 1, 0, 1]
]

for i in range(len(array1)):
    index = [ k for k,v in enumerate(array1[i]) if v ==0 ]
    print(i, index)
    
'''
outputs 
0 [2, 3]
1 [0, 1]
2 [0, 2]

'''


''' very primitive below, 
for i in range(0,3):
    for j in range(0,4):
        if (array1[i][j] == 1):
            print(i,j)
'''

'''
# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.nonzero.html
# not done yet 
# import numpy

array2 = numpy.array([  
  [1, 1, 0, 0],
  [0, 0, 1, 1],
  [0, 0, 0, 0]])
print(numpy.nonzero(array2))
'''

# https://stackoverflow.com/questions/27175400/how-to-find-the-index-of-a-value-in-2d-array-in-python

'''
outputs from for i,j loop

D:\Go-workspace\walter\coding\python>python locate_zero.py
0 0
0 1
1 2
1 3
2 1
2 3
'''
