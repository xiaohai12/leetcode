class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    elif j > 0:
                        dp[i][j] = dp[i][j - 1]
                    elif i > 0:
                        dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]