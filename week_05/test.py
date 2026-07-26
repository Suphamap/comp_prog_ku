target = int(input("Distance from starting point(m.): "))
current = 0
set_count = 0

while current != target:
    if current < target:
        current += 5
        print(current, end=" ")
        current -= 2
        print(current, end=" ")
        set_count += 1
    elif current > target:
        current -= 4
        print(current, end=" ")
        current += 3
        print(current, end=" ")
        set_count += 1

if not target == 0:
    print()
    print(f"Moved {set_count} set(s)")
else:
    print(current)
    print(f"Moved {set_count} set(s)")