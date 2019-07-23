class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        if l < 2 or numRows < 2:
            return s
        mod = 2 * numRows - 2
        ret = ['' for i in range(numRows)]
        for i in range(l):
            k = i % mod
            if k >= numRows:
                k = mod - k
            ret[k] += s[i]
        return ''.join(ret)
