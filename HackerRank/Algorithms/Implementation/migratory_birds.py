def migratory_birds(arr):
    arr_set = list(set(arr))
    _max = -float('inf')
    _max_id = 0
    for _id in arr_set[::-1]:
        _count = arr.count(_id)
        if _count >= _max:
            _max = _count
            _max_id = _id

    return _max_id

if __name__ == "__main__":
    _ = int(input())
    arr = list(map(int, input().split()))

    result = migratory_birds(arr)

    print(result)
    