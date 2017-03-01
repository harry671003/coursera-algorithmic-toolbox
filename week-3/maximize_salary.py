"""Maximum salary with given digits"""
from functools import cmp_to_key
from random import randint

def cmp(num1, num2):
    """Returns the shortest int starting with largest
    digit
    """

    if num1 == num2:
        return 0

    elif num1 + num2 < num2 + num1:
        return -1

    else:
        return 1


def max_salary(numbers):
    """Maximum Salary"""
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    sorted_numbers = sorted(numbers, key=cmp_to_key(cmp), reverse=True)

    return " | ".join(sorted_numbers)

def test():
    """Test function """
    numbers = []
    for i in range(100):
        numbers.append(randint(1, 1000))

    numbers.append(9)
    numbers.append(8)

    print(numbers)
    print_sep()
    print(
        max_salary(numbers)
    )

def print_sep():
    """Print Seperator"""
    print("")

if __name__ == "__main__":
    test()
