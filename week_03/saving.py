def compound_interest(p, r, n):
    a = p*((1 + (r/100))**n)
    return a

p = float(input("Enter initial amount in Baht: "))
r = float(input("Enter interest rate in percent: "))

print(f"Total amount after 1 year is {compound_interest(p, r, 1):.2f} Baht.")
print(f"Total amount after 5 years is {compound_interest(p, r, 5):.2f} Baht.")
print(f"Total amount after 10 years is {compound_interest(p, r, 10):.2f} Baht.")
print(f"Total amount after 20 years is {compound_interest(p, r, 20):.2f} Baht.")