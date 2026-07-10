def change(money, back_note):
    return money // back_note

money = int(input("Enter total money: "))
b500 = change(money, 500)
left = money - b500*500

b100 = change(left, 100)
left = left - b100*100
b20 = change(left, 20)
left = left - b20*20

b5 = change(left, 5)
left = left - b5*5
b1 = change(left, 1)


print(f"500: {b500}")
print(f"100: {b100}")
print(f" 20: {b20}")
print(f"  5: {b5}")
print(f"  1: {b1}")