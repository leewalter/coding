# python to locate 1 in a 2D array

array1 = [
  [1, 1, 0, 0],
  [0, 0, 1, 1],
  [0, 1, 0, 1]
]

for i in range(0,3):
    for j in range(0,4):
        if (array1[i][j] == 1):
            print(i,j)

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
