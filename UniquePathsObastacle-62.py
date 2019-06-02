class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] =1* (not obstacleGrid[i][j])
                elif i == 0 and j != 0:
                    if obstacleGrid[i][j-1]!=1:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j]  = 0
                elif i != 0 and j == 0:
                    if obstacleGrid[i-1][j]!=1:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j]  = 0
                else:
                    dp[i][j] = dp[i - 1][j]*(not obstacleGrid[i-1][j]) + dp[i][j - 1]*(not obstacleGrid[i][j-1])
        return dp[m - 1][n - 1]*(not obstacleGrid[m-1][n-1])