def counting_valleys(n, s):
    valleys = 0
    level = 0
    for char in s:
        if char == 'U': level += 1
        if char == 'D': level -= 1

        if level == 0 and char == 'U': valleys += 1
    return valleys

if __name__ == "__main__":
    n = int(input())
    s = input()

    result = counting_valleys(n, s)

    print(result)