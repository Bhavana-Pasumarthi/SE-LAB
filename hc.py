'hard coding variables'

import math
a = 1 
b = 2
c = 1 
d = b*b - 4*a*c 
if d >= 0 :
    print("THE ROOTS ARE:")
    print((-b - math.sqrt(d))/2*a)
    print((-b + math.sqrt(d))/2*a)
else :
    print("IMAGINARY ROOTS")