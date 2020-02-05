class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ind = []
        for i, s in enumerate(S):
            if s == C:
                ind.append(i)
        ret = []
        for i in range(len(S)):
            ret.append(self.MinInd(i, ind))
        return ret

    def MinInd(self, i, ind):
        temp = list(map(lambda x: abs(x - i), ind))
        return min(temp)

    
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        ret = [i for i in range(n)]
        pos = - n
        for i in range(n):
            if S[i]==C:
                pos = i
            ret[i] = i - pos
        for i in range(pos-1,-1,-1):
            if S[i] == C:
                pos = i
            ret[i] = min(ret[i],pos-i)
        return ret