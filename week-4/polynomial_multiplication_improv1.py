def match_length(poly1, poly2):
    """Returns a padded version of a list"""
    ret_poly1 = poly1
    ret_poly2 = poly2

    if len(poly1) < len(poly2):
        ret_poly1 = [0] * (len(poly2) - len(poly1)) + ret_poly1
    else:
        ret_poly2 = [0] * (len(poly1) - len(poly2)) + ret_poly2

    return (ret_poly1, ret_poly2)

def remove_leading_zeros(poly):
    """Remove the leading zeroes in a poly of an array"""
    for i in range(len(poly)):
        if poly[i] != 0:
            break

    # Return the non zero part of the polynomial
    return poly[i:]

class Polynomial:
    """Polynomial Definiton"""

    def __init__(self, polynomial):
        """Constructor"""
        self.__polynomial = remove_leading_zeros(polynomial)

    def __add__(self, other):
        """Polynomial Addition"""
        (poly1, poly2) = match_length(self.__polynomial, other.get_internal_notation())

        poly_sum = []
        for (c1, c2) in zip(poly1, poly2):
            poly_sum.append(c1 + c2)

        return Polynomial(poly_sum)

    def __mul__(self, other):
        """Polynomial Multiplication"""
        (poly1, poly2) = match_length(self.__polynomial, other.get_internal_notation())

        if(len(poly1)) == 0:
            return Polynomial([0])

        if len(poly1) == 1:
            return Polynomial([poly1[0] * poly2[0]])

        n = len(poly1)
        n_by_2 = len(poly1) // 2

        vd0 = Polynomial(poly1[(n - n_by_2):])
        vd1 = Polynomial(poly1[:(n - n_by_2)])

        ve0 = Polynomial(poly2[(n - n_by_2):])
        ve1 = Polynomial(poly2[:(n - n_by_2)])

        print(poly1, vd0, vd1)
        print(poly2, ve0, ve1)

        d1e1 = vd1 * ve1
        d1e0 = vd1 * ve0
        d0e1 = vd0 * ve1
        d0e0 = vd0 * ve0

        d1e1_x_n = Polynomial(d1e1.get_internal_notation() + ([0] * n))
        d1e0_d0e1_x_n_2 = Polynomial((d1e0 + d0e1).get_internal_notation() + ([0] * (n // 2)))

        return d1e1_x_n + d1e0_d0e1_x_n_2 + d0e0

    def get_internal_notation(self):
        """Returns the internal representation of a polynomial"""
        return self.__polynomial

    def __str__(self):
        """Returns string representaion
        of a polynomial
        """
        term_list = []
        max_power = len(self.__polynomial) - 1
        for coefficient in self.__polynomial:
            if coefficient == 1 and max_power != 0:
                term_list.append("x^%d" % (max_power,))

            elif coefficient != 0:
                if max_power == 0:
                    term_list.append("%d" % (coefficient,))
                else:
                    term_list.append("%dx^%d" % (coefficient, max_power))
            max_power -= 1

        if len(term_list) == 0:
            return "0"

        string_repr = ""
        for i in range(len(term_list)):
            if i > 0:
                string_repr += " + "
            string_repr += term_list[i]

        return string_repr

def test():
    p1 = Polynomial([4, 3, 2, 1])
    p2 = Polynomial([1, 2, 3, 4])

    print(p1 * p2)

if __name__ == "__main__":
    test()

