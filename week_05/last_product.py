def last_product(a, b, c):
    while a + b + c != 1:
        if (a >= b and a >= c) and b >= c:
            a -= 1
            b -= 1
            c += 1
        elif (a >= b and a >= c) and b <= c:
            a -= 1
            c -= 1
            b += 1
        elif (b >= a and b >= c) and c >= a:
            a += 1
            b -= 1
            c -= 1
        elif (b >= a and b >= c) and c <= a:
            a -= 1
            b -= 1
            c += 1
        elif (c >= a and c >= b) and a >= b:
            a -= 1
            b += 1
            c -= 1
        elif (c >= a and c >= b) and a <= b:
            a -= 1
            b += 1
            c += 1
        # print(a, b, c)

    if a > b and a > c:
        print("A")
    elif b > a and b > c:
        print("B")
    else:
        print("C")


a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

last_product(a, b, c)
