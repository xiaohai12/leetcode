class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        if col == 0:
            return False
        first = 0
        end = row - 1
        while first < end:
            mid = int((first + end + 1) / 2)
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                first = mid
            else:
                end = mid - 1
        left = 0
        right = col - 1
        while left < right:
            mid = int((left + right) / 2)
            if matrix[first][mid] == target:
                return True
            if matrix[first][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return matrix[first][left] == target
