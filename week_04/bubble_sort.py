"""Use the bubble sorting method"""
def sort_func(data):
    status = True
    count = 0
    while status:
        count = 0
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data[i+1], data[i] = data[i], data[i+1]
                count += 1
        if count == 0:
            status = False

    return data

data = input("Data: ").split()
data_int = [int(x) for x in data]
print(sort_func(data_int))
# a = int(input("A = "))
# b = int(input("B = "))
# c = int(input("C = "))