class Solution:
    ## DFS
    def getFactors(self, n: int) -> List[List[int]]:
        ret = []
        self.helper(ret, [], n, 2)
        return ret

    def helper(self, ret, tmp, end, start):
        if end <= 1:
            if len(tmp) > 1:
                ret.append(tmp.copy())
            else:
                return

        for i in range(start, end + 1):
            if end % i == 0:
                tmp.append(i)
                self.helper(ret, tmp, int(end / i), i)
                tmp.pop()

        # for factor in factors:
        #     if factor**2<n:
        #         ret.append([factor,int(n/factor)])
        #         sub = self.getFactors(int(n/factor))
        #         for items in sub:
        #             if items[0]>=factor:
        #                 ret.append([factor]+items)
        #     elif factor**2==n:
        #         ret.append([factor,factor])
        # return ret
