class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        zeros = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zeros.append([i, j])
        for pair in zeros:
            i, j = pair[0], pair[1]
            matrix[i] = [0] * col
            for k in range(row):
                matrix[k][j] = 0
        return matrix