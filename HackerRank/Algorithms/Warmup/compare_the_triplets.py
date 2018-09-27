def compare_the_triplets(a, b):
    score_a = 0
    score_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
    return [score_a, score_b]

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = compare_the_triplets(a, b)

    print(*result)