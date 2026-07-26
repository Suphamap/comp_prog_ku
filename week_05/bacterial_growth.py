def nb_year(p0, percent, aug, p):
    days = 0
    aug_add = p0
    while aug_add < p:
        aug_add = int(aug_add + (aug_add * (percent/100)) + aug)
        days += 1
        # print(aug_add)
    return int(days)

p0 = int(input("Enter p0: "))
percent = float(input("Enter percent: "))
aug = int(input("Enter aug: "))
p = int(input("Enter p: "))

print("Output =", nb_year(p0, percent, aug, p))