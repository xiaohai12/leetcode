class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        if n < 2:
            return dp[1]
        for i in range(2, n + 1):
            first = int(s[i - 1])
            second = int(s[i - 2:i])
            if first > 0 and first < 10:
                dp[i] += dp[i - 1]
            if second >= 10 and second < 27:
                dp[i] += dp[i - 2]
        return dp[n]

