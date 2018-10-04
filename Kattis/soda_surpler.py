e, f, c = map(int, input().split())

total = 0
empty = e + f
while empty >= c:
    empty -= c
    total += 1
    empty += 1

print(total)
