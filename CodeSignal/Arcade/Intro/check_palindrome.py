def checkPalindrome(inputString):
    if inputString == ''.join(reversed(inputString)):
        return True
    return False