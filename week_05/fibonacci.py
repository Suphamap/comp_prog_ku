x_0 = 0
x_1 = 1

n = int(input("Enter n: "))

for i in range(2, n+1):
    if i % 2 == 0:
        x_0 = x_1 + x_0
    else:
        x_1 = x_1 + x_0

if n % 2 == 0:
    print(f"x_{n} = {x_0}")
else:
    print(f"x_{n} = {x_1}")