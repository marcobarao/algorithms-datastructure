while True:
    highest = -float('inf')
    index_highest = -1
    for i in range(8):
        mountain_h = int(input())
        if mountain_h > highest:
            highest = mountain_h
            index_highest = i

    print(index_highest)