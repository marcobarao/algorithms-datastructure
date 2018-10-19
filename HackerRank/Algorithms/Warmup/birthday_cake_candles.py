def birthday_cake_candles(arr):
    return arr.count(max(arr))

if __name__ == "__main__":
    _ = input()
    arr = list(map(int, input().split()))

    result = birthday_cake_candles(arr)

    print(result)