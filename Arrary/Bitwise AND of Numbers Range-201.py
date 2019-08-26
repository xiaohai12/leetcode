class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        if m == n:
            return m
        p = 0
        while m >= 2 ** p:
            p += 1
        q = p
        while n >= 2 ** q:
            q += 1
        if q > p:
            return 0
        else:
            sub = 2 ** (p - 1)
            return sub + self.rangeBitwiseAnd(m - sub, n - sub)
