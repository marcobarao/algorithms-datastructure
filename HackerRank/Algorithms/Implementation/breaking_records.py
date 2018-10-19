def breaking_records(scores):
    _min = scores[0]
    _max = scores[0]
    break_min = 0
    break_max = 0

    for score in scores[1:]:
        if score > _max:
            _max = score
            break_max += 1
        elif score < _min:
            _min = score
            break_min += 1

    return [break_max, break_min]

if __name__ == "__main__":
    _ = input()
    scores = list(map(int, input().split()))

    result = breaking_records(scores)

    print(*result)
