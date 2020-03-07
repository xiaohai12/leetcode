class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand.sort()
        freq = {}
        rest = {}
        for num in hand:
            freq[num] = freq.get(num, 0) + 1
        for num in hand:
            if freq[num] != 0:
                for i in range(W):
                    if num + i in freq.keys():
                        freq[num + i] = freq[num + i] - 1
                    else:
                        return False
        return True

    ## the same as 659 
