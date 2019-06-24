class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        DP = triangle[-1]
        l = len(triangle)
        for layer in range(l-2,-1,-1):
            for node in range(0,layer+1):
                DP[node] = min(DP[node],DP[node+1])+triangle[layer][node]
        return DP[0]

    ## buttom to top DP, which is interesting! and also memnory save method (using only 1D DP array)