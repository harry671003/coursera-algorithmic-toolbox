"""Maximum pairwise products"""

def max_pairwise_product(sequence_1, sequence_2):
    """Maximum Pairwise product"""
    max_sum = 0

    # Sort the arrays
    sorted_sequence_1 = sorted(sequence_1)
    sorted_sequence_2 = sorted(sequence_2)

    for mem_1, mem_2 in zip(sorted_sequence_1, sorted_sequence_2):
        max_sum += mem_1 * mem_2
    return max_sum

def test():
    """Test function """
    test_sequence1 = [1, 3, -5]
    test_sequence2 = [-2, 4, 1]

    print(max_pairwise_product(test_sequence1, test_sequence2))

def print_sep():
    """Print Seperator"""
    print("")

if __name__ == "__main__":
    test()
