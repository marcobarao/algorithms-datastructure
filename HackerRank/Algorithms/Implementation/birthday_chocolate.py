def birthday(s, d, m):
    meeting = 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            meeting += 1
    
    return meeting

if __name__ == "__main__":
    _ = input()
    s = list(map(int, input().split()))
    d, m = map(int, input().split())

    result = birthday(s, d, m)

    print(result) 