class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == []:
            return False
        cols = len(matrix)
        rows = len(matrix[0])
        if rows == 0:
            return False

        for i in range(cols):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                return target in matrix[i]
            else:
                continue
        return False
