def fraction(p):
    x = p
    poly = (2*(x**4)) - (5*(x**3)) - (24*(x**2)) - (7*x) + (10)
    return poly

p = int(input("Input p: "))
print(f"Fraction = {fraction(p)}")
