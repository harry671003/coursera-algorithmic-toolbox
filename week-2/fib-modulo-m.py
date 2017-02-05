import itertools

# Calculate Fib(n) mod m
def fib(n, m):

    if m <= 1:
        return n % m

    # Pattern to identify the start of a new cycle
    pattern = [0, 1]

    # The cycle of Fib(n) % m
    cycle = [0, 1]

    # List to store the fib series
    fib_store = [0, 1]

    # Period count
    period = None
    breakAfter = 0

    for i in itertools.count(2):
        fib_store.append(fib_store[i-1] + fib_store[i-2])
        cycle = cycle + [fib_store[i] % m]

        # Check for the repetition of the cycle
        if len(cycle) > len(pattern) and cycle[len(cycle) - len(pattern):] == pattern:
            period = len(cycle) - len(pattern)
            break
    
    
    print("fib(%d) mod %d | %d" % (n, m, period))
    # print("Cycle: ", cycle)
    # print(fib_store)
    #print("Period: ", period)
    #print("")

    # return period

    equivalent = n % period
    # print("equivalent: %d" % (equivalent, ))
    # print("len(fib_store): %d" % (len(fib_store), ))

    return fib_store[equivalent] % m


def main():
    print(fib(1, 239))
    print(fib(2015, 3))
    print(fib(239, 1000))
    print(fib(2816213588, 30524))
    # for i in range(1, 50):
    #     fib(100, i)

    # fib(100, 11)

if __name__ == "__main__":
    main()