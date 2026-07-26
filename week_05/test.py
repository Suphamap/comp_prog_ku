import sys

msg = input("Enter a string: ")
n = int(input("Enter arrow's size (greater than 0): "))
if n <= 0:
    print("Size must be greater than 0.")
    sys.exit()


if n %2 != 0:
    for i in range(0, (n//2)+1):
        print(" "*i + msg)
    for i in range((n//2)-1, -1, -1):
        print(" "*i+ msg)
else:
    for i in range(0, (n//2)-1):
        print(" "*i + msg)
    print(" "*((n//2)-1) + msg)
    print(" " *((n//2)-1) + msg)
    for i in range((n//2)-2, -1, -1):
        print(" "*i+ msg)
