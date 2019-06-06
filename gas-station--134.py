class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        rest = []
        Min = 1000000000000
        ind = 0
        for i in range(l):
            rest.append(gas[i]-cost[i])
        cur = 0
        for j in range(l):
            cur +=rest[j]
            if Min>cur:
                Min = cur
                ind = j+1
        if cur <0:
            return -1
        else:
            return ind %l