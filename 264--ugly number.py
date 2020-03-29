class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ## nice dp problem with pointer !!!!!!!
        dp = [1 for i in range(n)]
        p2 = 0
        p5 = 0
        p3 = 0
        for i in range(1, n):
            dp[i] = min(dp[p2] * 2, min(dp[p3] * 3, dp[p5] * 5))
            if dp[i] == dp[p2] * 2:
                p2 += 1

            if dp[i] == dp[p3] * 3:
                p3 += 1

            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[-1]

