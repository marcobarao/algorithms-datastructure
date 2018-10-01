def sortByHeight(a):
    trees_index = []
    times = a.count(-1)
    times_copy = times
    while times:
        i = a.index(-1)
        trees_index.append(i)
        a[i] = 0
        times -= 1
    
    a = sorted(a)[times_copy:]

    for i in trees_index:
        a.insert(i, -1)

    return a

sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])