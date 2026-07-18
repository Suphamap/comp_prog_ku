def is_raining(x):
    if x == "y" or x == "Y":
        return True
    elif x == "N" or x == "n":
        return False
    else:
        return None
    
def round_days(minutes):
    if (minutes % 1440) >= 720:
        minutes = minutes + (1440 - (minutes % 1440))
        days = minutes // (24*60)
        return days
    else:
        return minutes // (24*60)

minutes = int(input("Minutes before due: "))
temperature = float(input("Temperature: "))
raining = input("Is it raining (y/n)? ")

days = round_days(minutes)

if days < 2:
    print(f">>> {days} days before due.")
    print(f">>> I will do the assignment.")
elif days > 5:
    print(f">>> {days} days before due.")
    print(f">>> I will not do the assignment.")
else:
    if temperature > 40 or (temperature > 25 and is_raining(raining)):
        print(f">>> {days} days before due.")
        print(f">>> I will not do the assignment.")
    else:
        print(f">>> {days} days before due.")
        print(f">>> I will do the assignment.")