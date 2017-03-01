"""Binary Search"""

def binary_search(arr, low, high, query):
    """Binary Search"""

    # End cases
    if not low <= high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == query:
        return mid


    if query < arr[mid]:
        return binary_search(arr, low, mid - 1, query)
    else:
        return binary_search(arr, mid + 1, high, query)


def test():
    """Test function """
    search_list = [3, 7, 11, 15, 20, 21, 35, 35, 40, 56, 70, 71, 71, 90]
    query_list = search_list + [12, 0, -1]

    for elem in query_list:
        try:
            binary_search_output = binary_search(search_list, 0, len(search_list) - 1, elem)
        except RecursionError as err:
            print("Error for %d" % elem)
            raise err

        if binary_search_output != -1:
            assert elem == search_list[binary_search_output]
        else:

            assert elem not in search_list

def print_sep():
    """Print Seperator"""
    print("")

if __name__ == "__main__":
    test()
