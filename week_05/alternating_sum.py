def alt_sum(n):
    result = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            result -= i
        else:
            result += i
    return result

n = int(input("Enter n of series: "))
print(f"Alternating Sum from 1 to {n} is {alt_sum(n)}")