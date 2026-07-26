def guessing(target):
    while True:
        num = int(input("Enter your guess (0 - 100): "))
        if num == target:
            print("Congratulations, your guess is correct.")
            break
        else:
            if not 0 <= num <= 100:
                print("Sorry, out of range, try again later.")
            elif num > target:
                print("Sorry, your guess is too high, try again later.")
            else:
                print("Sorry, your guess is too low, try again later.")

guessing(72)