police_dis = 0
criminal_dis = 100
time = 1

while police_dis < criminal_dis:
    police_dis += int(input("Input distance: "))
    print(f"Police distance: {police_dis}")
    criminal_dis += 2**time
    print(f"Criminal distance: {criminal_dis}")
    time += 1

print("Caught him!")