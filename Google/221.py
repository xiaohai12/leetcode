class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for i in range(m)] for i in range(n)]
        ## assume dp[i][j] is the maximun square till (i,j)
        Max = 0
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            Max = max(dp[i][0], Max)
        for i in range(m):
            dp[0][i] = int(matrix[0][i])
            Max = max(dp[0][i], Max)

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    Max = max(dp[i][j], Max)
        return Max ** 2