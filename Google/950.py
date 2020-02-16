class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if len(deck)<=1:
            return deck
        deck.sort()
        dp = [deck[-1]]
        for i in range(1,len(deck)):
            ret = []
            ret.append(deck[-i-1])
            ret.append(dp[-1])
            ret +=dp[:-1]
            dp = ret.copy()
        return dp