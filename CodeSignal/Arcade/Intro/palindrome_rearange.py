def palindromeRearranging(inputString):
    set_input = list(set(inputString))
    list_input = list(inputString)

    conditions = []
    for char in set_input:
        if list_input.count(char) % 2 == 0:
            conditions.append(True)
        else:
            conditions.append(False)

    if len(list_input) % 2 == 0:
        return all(conditions)

    return (True if conditions.count(False) == 1 else False)