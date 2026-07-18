def check_remaining(time):
    if time % 60 > 20:
        return time + (60 - (time % 60))
    else:
        return time - (time % 60)

time = int(input("How long have Buzz played? "))
round_time = check_remaining(time)
fee = 900

if 60*2 <= round_time < 60*4:
    fee = ((round_time // 60) * fee) * 0.9
elif round_time == 60*4:
    fee = ((round_time // 60) * fee) * 0.8
elif round_time >= 60*5:
    fee = ((round_time // 60) * fee) * 0.7
else:
    fee = ((round_time // 60) * fee)

print(f"Total price is {round(fee)} baht.")