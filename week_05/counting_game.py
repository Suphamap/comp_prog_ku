x = int(input("Enter x: "))
end = int(input("Enter y: "))
count = 0
divider = int(input("Enter p: "))

while x <= end:
    if x % divider == 0 and count == 0:
        x += 11
        count += 1
    elif (x + 1) % divider == 0:
        print(x, end=" ")
        x += 12
        count += 1
    else:
        print(x, end=" ")
        x += 1
        count += 1
