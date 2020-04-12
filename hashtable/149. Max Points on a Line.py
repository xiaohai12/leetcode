class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        ## use k = x/y to track line ---> regardless b
        l = len(points)
        Ret = 0
        for i in range(l - 1):
            p1 = points[i]
            Max = 0
            overlap = 0
            slope = {}
            for j in range(i + 1, l):
                p2 = points[j]
                x = p1[0] - p2[0]
                y = p1[1] - p2[1]
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                gcd = self.getGCD(x, y)
                if gcd != 0:
                    x /= gcd
                    y /= gcd  ## it is better than compute k since you need to consider y==0
                if x in slope.keys():
                    M = slope[x]
                    M[y] = M.get(y, 0) + 1
                else:
                    slope[x] = {y: 1}
                Max = max(Max, slope[x][y])
            Ret = max(Ret, Max + overlap + 1)
        return Ret

    def getGCD(self, x, y):
        if y == 0:
            return x
        return self.getGCD(y, x % y)