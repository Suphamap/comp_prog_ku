import sys

list_num = []

def average(data):
    return sum(data) / len(data)

num = input("Enter a number (just [Enter] to stop): ")

if num == "":
    print("Nothing to do.")
    sys.exit()

while num != "":
    num = float(num)
    list_num.append(num)
    num = input("Enter a number (just [Enter] to stop): ")

print(f"The maximum value is {max(list_num):.2f}")
print(f"The minimum value is {min(list_num):.2f}")
print(f"The average value is {average(list_num):.2f}")