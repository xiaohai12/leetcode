def generateMatrix(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1, 2], [4, 3]]
    else:
        LastMatrix = generateMatrix(n - 2)
        for i in range(n - 2):
            for j in range(n - 2):
                LastMatrix[i][j] += n ** 2 - (n - 2) ** 2
        matrix[0] = [i+1 for i in range(n)]
        matrix[n - 1] = [j for j in range(3 * n -2, 2 * n-2, -1)]

        for i in range(1, n - 1):
            matrix[i] = [4 * n - 3 - i] + LastMatrix[i - 1] + [n + i]
        return matrix

print(generateMatrix(4))
