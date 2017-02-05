def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def main():
    n = int(input('Enter a number'))
    print('fib(%d) = %d' % (n, fib(n)))

if __name__ == "__main__":
    main()