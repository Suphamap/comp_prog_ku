def factorial(x):
    fac = 1
    for j in range(1, x+1):
        fac = fac * j

    return fac

k = int(input("Input k: "))
result = 0
for i in range(1, k+1):
    fac = factorial(i)
    print(f"{i}! = {fac}")
    result += fac

print(f"Summation of factorial 1! to {k}! = {result}")