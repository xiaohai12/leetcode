class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if coins==[]:
            return -1
        inf = float('inf')
        dp = [inf for i in range(amount+1)]
        dp[0] = 0
        coins.sort()
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin<0:
                    continue
                dp[i] = min(dp[i],dp[i-coin]+1)
        if dp[-1]==inf:
            return -1
        return dp[-1]