n = int(input("Enter number: "))

for row in range(1, n+1):
    for col in range(row, row+n):
        print(col, end=" ")
    print()