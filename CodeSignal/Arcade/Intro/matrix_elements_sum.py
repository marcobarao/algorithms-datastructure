def matrixElementsSum(matrix):
    _sum = 0
    for row in matrix:
        c = row.count(0)
        while c > 0:
            row.remove()

matrixElementsSum([[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]])