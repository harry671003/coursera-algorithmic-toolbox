def fib(n):
    fib_n_2 = 0
    fib_n_1 = 1
    fib_n = None

    if n <= 1:
        return n

    sum = 1

    for i in range(2, n+1):
        fib_n = (fib_n_2 + fib_n_1) % 10
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
        sum = (sum + fib_n) % 10
        # print(fib_n)
        # print("fib_n_1: %d | fib_n_2: %d" %(fib_n_1, fib_n_2))
        # print("i: %d | fib_n: %d |sum: %d" %(i, fib_n, sum,))
    return sum

def main():
    n = int(input('Enter a number'))
    print('last_digit_sum_of_fib(%d) = %d' % (n, fib(n)))
    # print('fib(%d) = %d' % (3, fib(3)))

if __name__ == "__main__":
    main()