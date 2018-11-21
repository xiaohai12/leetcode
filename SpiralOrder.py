def spiralOrder(matrix):
    if len(matrix) == 1:
        return matrix[0]
    elif len(matrix) == 0:
        return []
    elif len(matrix[0])==1:
        return [x[0] for x in matrix]
    else:
        res = matrix[0]
        nextMatrix = []
        for i in range(1, len(matrix) - 1):
            if matrix[i][1:-1] !=[]:
                nextMatrix.append(matrix[i][1:-1])
        tmp = matrix[-1].copy()
        tmp.reverse()
        res = res + tmp
        for i in range(len(matrix)-2, 0, -1):
            res.append(matrix[i][0])
        return res + spiralOrder(nextMatrix)

print(spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))