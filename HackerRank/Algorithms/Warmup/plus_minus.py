def plus_minus(arr):
    p = 0
    n = 0
    z = 0
    for num in arr:
        if num > 0:
            p += 1 / len(arr)
        elif num < 0:
            n += 1 / len(arr)
        else:
            z += 1 / len(arr)
            
    print("{:.6f}".format(p))
    print("{:.6f}".format(n))
    print("{:.6f}".format(z))

if __name__ == "__main__":
    _ = input()
    arr = list(map(int, input().split()))

    plus_minus(arr)
