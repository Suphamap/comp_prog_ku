injured = input("Is Buzz injured (y/n)? ")

if injured == "y":
    print("Not available")
else:
    on_time = input("Is Buzz late for the training (y/n)? ")
    if on_time == "n":
        print("Starter")
    else:
        perform = input("Did Buzz perform well in training (y/n)? ")
        if perform == "y":
            print("Substitute")
        else:
            print("Not selected")