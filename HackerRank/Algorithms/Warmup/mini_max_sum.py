def mini_max_sum(arr):
    _max = -float('inf')
    _min = float('inf')
    for i in range(len(arr)):
        copy = arr.copy()
        del(copy[i])
        _sum = sum(copy)
        _max = max(_max, _sum)
        _min = min(_min, _sum)
    
    print('{} {}'.format(_min, _max))

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    mini_max_sum(arr)
