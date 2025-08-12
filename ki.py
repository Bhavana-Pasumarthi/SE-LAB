'keyboard input'

import math
a = float(input("ENTER VALUE OF a:"))
b = float(input("ENTER VALUE OF b:"))
c = float(input("ENTER VALUE OF c:"))
d = b*b - 4*a*c 
if d >= 0 :
    print("THE ROOTS ARE:")
    print((-b - math.sqrt(d))/2*a)
    print((-b + math.sqrt(d))/2*a)
else:
    print("IMAGINARY ROOTS")