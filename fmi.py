"read from a file: for multiple sets of input"

import math

def quadraticroots(a, b, c):
    d = b*b - 4*a*c 

    if d >= 0:
        print("THE ROOTS ARE:")
        print((-b - math.sqrt(d))/(2*a))
        print((-b + math.sqrt(d))/(2*a))
    else:
        print("IMAGINARY ROOTS")

with open("Multipleset.txt", "r") as f:
    for line in f:
        a, b, c = map(float, line.strip().split())
        quadraticroots(a, b, c)


