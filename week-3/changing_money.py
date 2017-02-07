"""Changing money"""

def min_denominations(amount, denominations):
    """
    Change for money
    calculate the minimum change that is required for
    amount in the given denominations

    Params:
    amount -- total amount
    denominations -- allowed denominations

    Returns:
    min number of coins
    """

    change = {}
    total_count = 0

    if amount == 0:
        return change, total_count

    # Sort the denominations
    sorted_denominations = sorted(denominations, reverse=True)

    # iterate
    for denomination in sorted_denominations:
        count = amount // denomination
        amount = amount % denomination

        if count != 0:
            change[denomination] = count
            total_count += count

        if amount == 0:
            break

    if amount != 0:
        return -1
    else:
        return change, total_count


def test():
    """ Test function """
    denominations = [1, 5, 10]
    amount = 999

    print(min_denominations(amount, denominations))

if __name__ == "__main__":
    test()
