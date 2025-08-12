'read from a file: for single set of input'

import math

with open("Singleset.txt", "r") as f:
    line = f.readline()
    a, b, c = map(float, line.strip().split())

d = b*b - 4*a*c 

if d >= 0:
    print("THE ROOTS ARE:")
    print((-b - math.sqrt(d))/2*a)
    print((-b + math.sqrt(d))/2*a)
else:
    print("IMAGINARY ROOTS")