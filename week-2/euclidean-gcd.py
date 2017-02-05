def gcd(n1, n2):
    # Swap numbers in case n1 < n2
    if n1 < n2:
        temp = n1
        n1 = n2
        n2 = temp
    
    print("n1: %d | n2: %d" % (n1, n2))

    if n2 == 0:
        return n1
    
    return gcd(n2, n1 % n2)

def main():
    token = input('Enter 2 number: ')
    (n1, n2) = token.split()
    print('gcd(%s, %s) = %d' % (
        n1, 
        n2, 
        gcd(
            int(n1), 
            int(n2)
        )
    ))

def test():
    gcd(10**100000 + 234, 5 ** 4 + 3)

if __name__ == "__main__":
    test()