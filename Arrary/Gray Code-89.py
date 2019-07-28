class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==0:
            return [0]
        dp = [[] for i in range(n)]
        dp[0] = [0,1]
        for i in range(1,n):
            dp[i] +=dp[i-1]
            for j in range(len(dp[i-1])-1,-1,-1):
                dp[i].append(dp[i-1][j]+2**i)
        return dp[-1]