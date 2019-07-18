class Solution:
    def countAndSay(self, n: int) -> str:
        dp = ['' for i in range(n)]
        dp[0] = '1'
        for i in range(1,n):
            tmp = dp[i-1][0]
            count = 0
            for char in dp[i-1]:
                if tmp !=char:
                    dp[i]+=str(count)+tmp
                    tmp = char
                    count = 1
                else:
                    count +=1
            dp[i]+=str(count)+tmp

        return dp[-1]