class Solution:
    def numSquares(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp[0] = 0
        i = 1

        for i in range(1, n + 1):
            j = 1
            Min = 2 ** 31 - 1
            while j * j <= i:
                Min = min(1 + dp[i - j * j], Min)
                j += 1
            dp[i] = Min

        return dp[-1]
