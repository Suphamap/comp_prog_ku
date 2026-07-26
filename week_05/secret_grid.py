n = int(input("Enter number: "))

for row in range(n):
    for col in range(n):
        if row % 2 == 0:
            if col % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        else:
            if col % 2 == 0:
                print("0", end=" ")
            else:
                print("1", end=" ")  
    print()