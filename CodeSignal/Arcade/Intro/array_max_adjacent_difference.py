def arrayMaximalAdjacentDifference(inputArray):
    _max = -float('inf')
    for i in range(len(inputArray) - 1):
        calc = abs(inputArray[i] - inputArray[i+1])
        if calc > _max:
            _max = calc

    return _max
