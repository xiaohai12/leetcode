class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        Minlen = [ triangle[-1][i] for i in range(n)]
        for layer in range(n-2,-1,-1):
            for i in range(layer+1):
                Minlen[i] = min(Minlen[i],Minlen[i+1]) + triangle[layer][i]
        return Minlen[0]