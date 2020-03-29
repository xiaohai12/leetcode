class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0 for i in range(n)]
        dp[0] = grid[0][0]
        ## update row by row 
        for i in range(1, n):
            dp[i] = grid[0][i] + dp[i - 1]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]
        '''
        m,n = len(grid),len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
                elif i>0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif j>0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]

       64. Minimum Path Sum return dp[-1][-1]

        '''
