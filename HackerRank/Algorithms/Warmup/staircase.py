def staircase(n):
    for i in range(1, n+1):
        print("{0:>{width}}".format('#' * i, width=n))

if __name__ == "__main__":
    n = int(input())

    staircase(n)