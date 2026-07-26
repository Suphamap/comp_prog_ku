total = 0

item = int(input("How many food you have: "))

for i in range(1, item+1):
    value = int(input(f"food #{i}'s value: "))
    status = int(input(f"food #{i}'s status: "))
    if status == 1:
        total += value
    elif status == -1:
        total -= value
print(total)