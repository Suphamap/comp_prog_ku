def simple_interest(p,r,t):
    interest = p*(r/100)*t
    total = p+interest
    return total

def compound_interest(p,r,t):
    a = p*((1 + (r/100))**t)
    return a

# main program
principal = float(input("Enter principle: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))

print(f"Return money for simple interest calculation is {simple_interest(principal, rate, time):.2f} Baht.")
print(f"Return money for compound interest calculation is {compound_interest(principal, rate, time):.2f} Baht.")