import math

def thousands(num):
    return math.floor(num/1000)

def hundreds(num):
    results = num - thousands(num)*1000
    return math.floor(results/100)

def tens(num):
    results = num - hundreds(num)*100 - thousands(num)*1000
    return math.floor(results/10)

def ones(num):
    results = num - hundreds(num)*100 - thousands(num)*1000 - tens(num)*10
    return results

def sum_digits(num):
    return ones(number) + tens(number) + hundreds(number) + thousands(number)
    
# main program
number = int(input("Enter a number (0 to 9999): "))
print(f"Ones place is {ones(number)}.")
print(f"Tens place is {tens(number)}.")
print(f"Hundreds place is {hundreds(number)}.")
print(f"Thousands place is {thousands(number)}.")
print(f"Sum of all digits is {sum_digits(number)}.")