def adjacentElementsProduct(inputArray):
    _max = -float('inf')
    for i in range(len(inputArray)-1):
        prod = inputArray[i] * inputArray[i+1]
        if prod > _max:
            _max = prod
    return _max

if __name__ == "__main__":
    array = list(map(int, input().split()))

    print(adjacentElementsProduct(array))
        