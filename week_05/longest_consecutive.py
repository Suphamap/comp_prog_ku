def longest_consecutive(data):
    count = 1
    max_count = 1
    num = data[0]
    for n in range(len(data)-1):
        if data[n] == data[n+1]:
            count += 1
            if count > max_count:
                num = data[n]
                max_count = count
        else:
            count = 1
    return max_count, num

list_num = []

num = int(input())
while num != 0:
    list_num.append(num)
    num = int(input())

max_count, max_num = longest_consecutive(list_num)
print(max_count)
print(max_num)