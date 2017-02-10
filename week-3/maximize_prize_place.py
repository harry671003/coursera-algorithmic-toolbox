"""Maximum price place"""

def max_price_place(total_candies):
    """Maximum Price Place"""
    positions = {
        "count": 0,
        "prizes": []
    }

    i = 1
    while total_candies > 0:
        if i < (total_candies - i):
            positions["prizes"].append(i)
            total_candies -= i
            positions["count"] += 1
        else:
            positions["prizes"].append(total_candies)
            total_candies = 0
            positions["count"] += 1
        i += 1

    return positions

def test():
    """Test function """
    total_candies = 10e9
    print(max_price_place(total_candies))

def print_sep():
    """Print Seperator"""
    print("")

if __name__ == "__main__":
    test()
