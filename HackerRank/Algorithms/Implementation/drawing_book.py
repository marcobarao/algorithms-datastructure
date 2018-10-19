def page_count(n, p):
    half = n / 2
    if  half >= p:
        return p // 2
    else:
        if n % 2 == 0:
            return (n-p+1) // 2
        return (n-p) // 2

if __name__ == '__main__':
    n = int(input())
    p = int(input())

    result = page_count(n, p)

    print(result)