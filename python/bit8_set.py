# to test if bit 8 is set to see if big or small ediian

def is_bit8_set(n):
    bit8 = bool(n & 0b10000000)
    print(" n ", n , " has bit 8 set = ", bit8)
    return(bit8)

for n in range(126,130):
    is_bit8_set(n)
    
'''
128 = 1000 0000

 n  126  has bit 8 set =  False
 n  127  has bit 8 set =  False
 n  128  has bit 8 set =  True
 n  129  has bit 8 set =  True
'''
