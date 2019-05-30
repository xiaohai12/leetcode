class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        MaxCur = 0
        Max = 0
        for i in range(0,len(prices)-1):
            MaxCur = max(0,MaxCur+prices[i+1]-prices[i])
            Max = max(Max,MaxCur)
        return Max

        comment:
        '''
        if prices == []:
            return 0
        Max = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(price, min_price)
            # compute current min price
            Max = max(Max, price - min_price)
        return Max
