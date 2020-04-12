class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            freq[c] = freq.get(c, 0) + 1

        start = 0
        while start < len(s) and s[start] not in freq.keys():
            start += 1

        Min = len(s)
        ret_s = -1
        ret_e = -1

        for i in range(len(s)):
            c = s[i]
            if c in freq.keys():
                freq[c] -= 1

                while freq[c] <= 0 and self.check(freq):
                    if Min >= i - start + 1:
                        ret_s = start
                        ret_e = i
                        Min = i - start + 1

                    freq[s[start]] += 1

                    start += 1
                    while start < len(s) and s[start] not in freq.keys():
                        start += 1
        if ret_s == -1:
            return ''
        return s[ret_s:ret_e + 1]

    def check(self, freq):
        for key in freq.keys():
            if freq[key] > 0:
                return False
        return True


