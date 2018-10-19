def makeArrayConsecutive2(statues):
    _min = min(statues)
    _max = max(statues)

    return len(range(_min, _max+1)) - len(statues)