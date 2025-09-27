# types of functions

# 1. In-Built function ==> int(), len( )
# 2. Module function
# 3. User- Defined function


# 2. Module function

# import math
# print(dir(math))

from math import sqrt
print(sqrt(4))
print(sqrt(8))


from math import * # ==> this will import all the functions of math
print(sqrt(4))
print(sqrt(8))

# 3. User- Defined function

def Sum(a,b=8):
    print(a+b)

Sum(2,4) 
Sum(2)       