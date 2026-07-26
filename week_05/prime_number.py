def is_prime(n):
    status = True
    # if n <= 1:
    #     return False
    for i in range(2, (n//2)+1):
        if n % i == 0:
            status = False
            break

    return status

n = int(input("Enter positive N: "))
n = n - 1

while not is_prime(n):
    n -= 1

print(n)