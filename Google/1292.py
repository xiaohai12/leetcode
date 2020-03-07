class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if mat == []:
            return 0
        n = len(mat)
        m = len(mat[0])
        Sum = [[0 for i in range(m + 1)] for j in range(n + 1)]
        ## Sum[i][j] = i*j area sum
        l = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                Sum[i][j] = Sum[i - 1][j] + Sum[i][j - 1] - Sum[i - 1][j - 1] + mat[i - 1][j - 1]
                if i >= l and j >= l and Sum[i][j] - Sum[i - l][j] - Sum[i][j - l] + Sum[i - l][j - l] <= threshold:
                    l += 1  ## this is trick
        return l - 1

        ### normal way
#         binary search: l = 0, h = min(m,n)
#         check(mid), if true, l = mid +1, else: h = mid -1

#     def check(self,mid,Sum):
#         for i in range(mid,n):
#             for j in range(mid,m)::
#                     return Sum[i][j]-Sum[i-l][j]-Sum[i][j-l]+Sum[i-l][j-l] <=threshold:

