def lol(data):
    consecutive = []
    count = 1
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            count += 1
        else:
            consecutive.append(count)
            count = 1

    consecutive.append(count)
    if not data == []:
        return max(consecutive)
    else:
        return 0

list_num = []

try:
    num = float(input("Enter number: "))
    while num != -1:
        list_num.append(num)
        num = float(input("Enter number: "))
except:
    None

# print(list_num)
print(lol(list_num))
# print(lol([-5, -6, -7, -10, 6, 9, 2, 3]))