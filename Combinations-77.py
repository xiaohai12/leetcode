# class Solution:
def combine(n: int, k: int):
    total = [i + 1 for i in range(n)]
    dp = [[] for i in range(k + 1)]
    dp[0] = []
    dp[1] = [[i + 1] for i in range(n)]
    for i in range(2, k + 1):
        if i <= round(int(n) / 2):
            for j in range(len(dp[i - 1])):
                for t in range(1, n + 1):
                    temp = dp[i - 1][j].copy()
                    if t > max(dp[i - 1][j]):
                        temp.append(t)
                        dp[i].append(temp)
        elif i==n:
            dp[i] = [total]
        else:
            dp[i] = [[n for n in total if n not in list_b] for list_b in dp[n - i]]
    return dp[k]

a = combine(2,2)
print(a)