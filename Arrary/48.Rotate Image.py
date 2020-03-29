class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l!=1:
            for i in range(l-1):
                for j in range(l-i-1):
                    matrix[i][j],matrix[l-1-j][l-1-i] = matrix[l-1-j][l-1-i],matrix[i][j]
            for i in range(int(l/2)):
                matrix[i],matrix[l-1-i] = matrix[l-1-i],matrix[i]