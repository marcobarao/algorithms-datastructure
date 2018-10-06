n = int(input())

divisor = 3600
for _ in range(2):
    print("{}".format(n // divisor), end=":")
    n = n % divisor
    divisor //= 60
print("{}".format(n // divisor), end="\n")
