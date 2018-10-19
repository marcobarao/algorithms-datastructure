def avoidObstacles(inputArray):
    set_input = set(sorted(inputArray))
    for i in range(1, max(inputArray)+1):
        set_generated = set(range(0, max(inputArray) + 1, i))

        if set_input.difference(set_generated) == set_input:
            return i
    return max(inputArray) + 1

print(avoidObstacles(list(map(int, input().split()))))
