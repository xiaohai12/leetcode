class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0

        ## three dp list
        m, n = len(matrix), len(matrix[0])
        height = [0 for i in range(n)]  ## continous '1' for each col
        left = [0 for i in range(n)]  ## leftmost index
        right = [n for i in range(n)]  ## right most index

        Area = 0
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                Area = max(Area, height[j] * (right[j] - left[j]))
        return Area 