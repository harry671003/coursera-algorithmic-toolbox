"""Polynomial Multiplication"""

def left_pad(poly1, poly2):
    # Left Pad the polynomials
    if len(poly1) < len(poly2):
        poly1 = [0] * (len(poly2) - len(poly1)) + poly1
    else:
        poly2 = [0] * (len(poly1) - len(poly2)) + poly2

    return poly1, poly2

def multiply(poly1, poly2):
    """Polynomial multiplication"""
    poly1, poly2 = left_pad(poly1, poly2)

    product = [0] * (2 * len(poly1) - 1)

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            product[i+j] += poly1[i] * poly2[j]
    print(product)

def test():
    """Test function """
    poly1 = [2, 3, 6]
    poly2 = [4, 3, 7]

    multiply(poly1, poly2)

def print_sep():
    """Print Seperator"""
    print("")

if __name__ == "__main__":
    test()
