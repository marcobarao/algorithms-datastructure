def addBorder(picture):
    width = len(picture[0]) + 2

    for i in range(len(picture)):
        picture[i] = picture[i].center(width, '*')
        
    picture.insert(0, '*' * width)
    picture.append('*' * width)

    return picture

addBorder(['abc', 'def'])