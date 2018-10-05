import itertools
def divisible_sum_pairs(arr, k):
    arr.sort()
    meet = 0
    for i, j in itertools.combinations(range(len(arr)), 2):
        if (arr[i] + arr[j]) % k == 0:
            meet += 1
    
    return meet

if __name__ == "__main__":
    _, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = divisible_sum_pairs(arr, k)

    print(result)
