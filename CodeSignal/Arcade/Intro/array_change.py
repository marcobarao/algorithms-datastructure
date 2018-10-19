def arrayChange(inputArray):
    moves = 0
    for i in range(len(inputArray)-1):
        if inputArray[i] > inputArray[i+1]:
            moves += inputArray[i] + 1 - inputArray[i+1]
            inputArray[i+1] = inputArray[i] + 1
        elif inputArray[i] == inputArray[i+1]:
            inputArray[i+1] += 1
            moves += 1
    return moves
