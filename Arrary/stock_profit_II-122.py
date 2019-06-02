class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        MaxCur = 0
        for i in range(0,len(prices)-1):
            MaxCur += max(0,prices[i+1]-prices[i])
        return MaxCur
    # seperate the list into several Incremental sequence, in each sublist, buy first sell last one.
