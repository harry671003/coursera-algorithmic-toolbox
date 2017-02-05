def fib(m, n):
    assert(m <= n)

    fib_n_2 = 0
    fib_n_1 = 1
    fib_n = None

    if n <= 1:
        return n

    for i in range(2, m + 1):
        fib_n = (fib_n_2 + fib_n_1) % 10
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
    
    sum = fib_n
    for i in range(m + 1, n + 1):
        fib_n = (fib_n_2 + fib_n_1) % 10
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
        sum = (sum + fib_n) % 10
        # print(fib_n)
        # print("fib_n_1: %d | fib_n_2: %d" %(fib_n_1, fib_n_2))
        # print("i: %d | fib_n: %d |sum: %d" %(i, fib_n, sum,))
    return sum

def main():
    (m, n) = (input('Enter m and n: ').split())

    print('last_digit_sum_of_fib(%d, %d) = %d' % ( int(m), int(n), fib(int(m), int(n)) ))
    # print('fib(%d) = %d' % (3, fib(3)))

if __name__ == "__main__":
    main()