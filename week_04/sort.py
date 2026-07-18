def sort_func(a, b, c):
    if a > b and a > c:
        if b > c:
            return c, b, a
        else:
            return b, c, a
    elif b > a and b > c:
        if a > c:
            return c, a, b
        else:
            return a, c, b
    else:
        if a > b:
            return b, a, c
        else:
            return a, b, c


a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

sort_a, sort_b, sort_c = sort_func(a, b, c)
print(f"{sort_a} {sort_b} {sort_c}")