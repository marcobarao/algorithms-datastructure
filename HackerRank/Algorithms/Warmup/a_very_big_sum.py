def a_very_big_sum(arr):
    return sum(arr)

if __name__ == "__main__":
    _ = input()
    arr = list(map(int, input().split()))

    result = a_very_big_sum(arr)

    print(result)