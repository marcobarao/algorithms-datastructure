def diagonal_difference(arr):
    diag_a = 0
    diag_b = 0
    for i in range(len(arr)):
        diag_a += int(arr[i][i])
        diag_b += arr[i][len(arr) - (i + 1)]
    
    return abs(diag_a - diag_b)

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    result = diagonal_difference(arr)

    print(result)