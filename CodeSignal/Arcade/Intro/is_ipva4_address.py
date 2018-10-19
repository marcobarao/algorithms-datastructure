def isIPv4Address(inputString):
    try:
        notations = list(map(int, inputString.split('.')))
    except:
        return False

    if len(notations) != 4:
        return False
    for notation in notations:
        if notation > 255 or notation < 0:
            return False
    return True
