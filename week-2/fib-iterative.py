def fib(n):
    fib_n_2 = 0
    fib_n_1 = 1
    fib_n = None

    if n <= 1:
        return n

    for i in range(1, n+1):
        fib_n = (fib_n_2 + fib_n_1) % 10
        fib_n_1 = fib_n_2
        fib_n_2 = fib_n
    return fib_n

def main():
    n = int(input('Enter a number'))
    print('fib(%d) = %d' % (n, fib(n)))

if __name__ == "__main__":
    main()