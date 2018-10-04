p = int(input())

for _ in range(p):
    k, n = map(int, input().split())
    s1 = (1 + n) * n // 2
    print("{0} {1} {2} {3}".format(k, s1, s1*2-n, s1*2))