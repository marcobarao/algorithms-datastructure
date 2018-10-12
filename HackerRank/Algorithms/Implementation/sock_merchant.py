def sock_merchant(arr):
    set_arr = set(arr)
    return sum([(arr.count(color) // 2) for color in set_arr])

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))

    result = sock_merchant(arr)

    print(result)