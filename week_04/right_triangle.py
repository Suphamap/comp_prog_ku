import sys

def read_nonnegative(arg):
    a = float(input(arg))
    check_neg(a)
    return a

def check_neg(x):
    if x < 0:
        print("Invalid value: input must be nonnegative")
        sys.exit()

def is_triangle(a, b, c):
    if a < (b+c) and b < (a+c) and c < (a+b):
        return True
    else:
        return False

def is_right_triangle(a, b, c):
    if a**2 == b**2 + c**2:
        return True
    elif b**2 == a**2 + c**2:
        return True
    elif c**2 == a**2 + b**2:
        return True
    else:
        return False



# main program
a = read_nonnegative("Enter 1st line's length: ")
b = read_nonnegative("Enter 2nd line's length: ")
c = read_nonnegative("Enter 3rd line's length: ")

if is_triangle(a, b, c):
    if is_right_triangle(a, b, c):
        print("It's a right triangle.")
    else:
        print("It's a triangle but not a right triangle.")
else:
    print("It's not a triangle.")
