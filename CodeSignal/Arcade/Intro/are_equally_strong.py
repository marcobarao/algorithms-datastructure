def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (True if max(yourLeft, yourRight) == max(friendsLeft, friendsRight) and yourLeft + yourRight == friendsLeft + friendsRight else False)
