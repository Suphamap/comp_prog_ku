def count_digits(number):
    number = abs(number)
    divider = 1
    count = 0
    while number / divider >= 1:
        count += 1
        divider = divider * 10
    return 1 if number == 0 else count


def get_last_digit(n):
    """
    Get last digit in number
    :params number is an integer
    :return last digit in number

    >>> get_last_digit(41)
    1
    >>> get_last_digit(394)
    4
    >>> get_last_digit(1020)
    0
    """
    return n % 10



def get_distribution(number):
    """
    Return string showing distribution of number
    :params number (int): a number to find distribution
    :return string
    >>> get_distribution(21)
    '1x10^0 + 2x10^1'
    >>> get_distribution(306)
    '6x10^0 + 0x10^1 + 3x10^2'
    >>> get_distribution(12201)
    '1x10^0 + 0x10^1 + 2x10^2 + 2x10^3 + 1x10^4'
    """
    result = ""
    digits = count_digits(number)
    for i in range(digits):
        if i != (digits - 1):
            result += f"{get_last_digit(number)}x10^{i} + "
            number = number // 10
        else:
            result += f"{get_last_digit(number)}x10^{i}"
    return result
# Main
n = int(input("Input number: "))
print(f"{n} = {get_distribution(n)}")
