def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i,n):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp;
    for i in range(n):
        matrix[i].reverse()


    return matrix;


a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[7,4,1],[8,5,2],[9,6,3]]

rotate(a)
