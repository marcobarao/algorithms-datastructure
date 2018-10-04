def kangaroo(x1, v1, x2, v2):
    if x2 > x1 and v2 > v1 or v2 - v1 == 0:
        return 'NO'
    
    if (x1 - x2) % (v2 - v1) == 0:
        return 'YES'
    return 'NO'

if __name__ == "__main__":
    x1, v1, x2, v2 = map(int, input().split())

    result = kangaroo(x1, v1, x2, v2)

    print(result)
