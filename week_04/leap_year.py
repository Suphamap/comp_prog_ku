import sys

def is_positive(y):
    if y < 1:
        return False
    else:
        return True 

def is_leap_year(y):
    if y >= 1752:
        if y % 400 == 0:
            return True
        elif (y % 4 == 0) and (y % 100 != 0):
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False

year = int(input("What is the year in AD? "))
if not is_positive(year):
    print(f"Invalid input: input year must be a positive integer")
    sys.exit()

if is_leap_year(year):
    print(f"AD {year} is a leap year")
else:
    print(f"AD {year} is not a leap year")