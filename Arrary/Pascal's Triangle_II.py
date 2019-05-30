class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        best solution
        res = [1]
        for i in range(1,rowIndex+1):
            res = list(map(lambda x,y:x+y,res+[0],[0]+res))
        return res
        '''
        dp = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for i in range(1, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[rowIndex]
