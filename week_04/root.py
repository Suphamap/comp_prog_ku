import sys
from math import sqrt
a = float(input("Value of 1st coefficient: "))

if a == 0:
    print("1st coefficient can't be zero. Program exits.")
    sys.exit()

b = float(input("Value of 2nd coefficient: "))
c = float(input("Value of 3rd coefficient: "))

d = ((b**2) - 4*a*c)

if d > 0:
    sol_1 = (-b + (d**(1/2))) / (2*a)
    sol_2 = (-b - (d**(1/2))) / (2*a)
    print(f"There are two real roots: {sol_1:.3f} and {sol_2:.3f}")
elif d == 0:
    sol_1 = (-b)/(2*a)
    print(f"Only one real root: {sol_1:.3f}")
else:
    if a < 0:
        print(f"There are two complex roots: {(-b)/(2*a):.3f}+{(sqrt(-d))/(-2*a):.3f}i and {(-b)/(2*a):.3f}{(sqrt(-d))/(2*a):.3f}i")
    else:
        print(f"There are two complex roots: {(-b)/(2*a):.3f}+{(sqrt(-d))/(2*a):.3f}i and {(-b)/(2*a):.3f}{(sqrt(-d))/(-2*a):.3f}i")
