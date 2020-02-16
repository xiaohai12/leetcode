class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j]>0 and j>0 and i>0):
                    matrix[i][j] = min(matrix[i-1][j-1],min(matrix[i-1][j],matrix[i][j-1])) + 1
                ret +=matrix[i][j]
        return ret