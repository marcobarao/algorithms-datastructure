def apple_orange(s, t, a, b, apples, oranges):
    al = 0
    ol = 0

    for apple in apples:
        if apple + a >= s and apple + a <= t:
            al += 1

    for orange in oranges:
        if orange + b >= s and orange + b <= t:
            ol += 1

    return [al, ol]

if __name__ == "__main__":
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    _ = input()
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    result = apple_orange(s, t, a, b, apples, oranges)

    print(*result, sep="\n")


