def allLongestStrings(inputArray):
    _max = max([len(string) for string in inputArray])
    return [string for string in inputArray if len(string) == _max]