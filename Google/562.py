class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if M==[]:
            return 0
        n = len(M)
        m = len(M[0])
        dp = [[[0 for i in  range(4)] for i in range(1+m)] for i in range(n+1)]
        direction = [[0 for i in range(1+m)] for i in range(n+1)]
        ## dp[i][j] means the longest line till M[i][j]
        Max = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if M[i-1][j-1] == 0:
                    continue
                else:
                    dp[i][j][0] = dp[i][j-1][0]+1 #hor
                    dp[i][j][1] = dp[i-1][j][1]+1 #ver
                    dp[i][j][2] = dp[i-1][j-1][2]+1 #dig
                    if j<m:
                        dp[i][j][3] = dp[i-1][j+1][3]+1 #dig
                    Max = max(Max,max(dp[i][j]))
        return Max