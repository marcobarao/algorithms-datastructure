from functools import reduce
from fractions import gcd

def between_two_sets(a, b):
    lcm_a = reduce(lambda x, y: x * y // gcd(x, y), a)
    gcd_b = reduce(gcd, b)
    gcd_b_copy = gcd_b
    return sum(1 for x in range(lcm_a, gcd_b + gcd_b_copy, lcm_a) if gcd_b % x == 0)

if __name__ == "__main__":
    _ = input()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = between_two_sets(a, b)

    print(result)