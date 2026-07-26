def count_digits(number):
    """
    Get number of digits in number
    :params number is an integer
    :return number of digits in number

    >>> count_digits(41)
    2
    >>> count_digits(-41)
    2
    >>> count_digits(1)
    1
    """
    number = abs(number)
    divider = 1
    count = 0
    while number / divider >= 1:
        count += 1
        divider = divider * 10
    return 1 if number == 0 else count

# Main
number = int(input("Enter number: "))
print(f"There are {count_digits(number)} digits in {number}")