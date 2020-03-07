class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        c = 0
        for word in words:
            if self.check(S, word):
                c += 1
        return c

    def check(self, S, word):
        i, j, n, m = 0, 0, len(S), len(word)
        if m > n:
            return False
        for i in range(n):
            if j < m and S[i] == word[j]:
                j += 1
            elif S[i - 1:i + 2] == S[i] * 3:
            elif S[i] * 3 == S[i - 2:i + 1]:
                return False
        return j == m

        """
        def check(self, S, W):
        i, j, i2, j2, n, m = 0, 0, 0, 0, len(S), len(W)
        while i < n and j < m:
            if S[i] != W[j]: return False
            while i2 < n and S[i2] == S[i]: i2 += 1
            while j2 < m and W[j2] == W[j]: j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j): return False
            i, j = i2, j2
        return i == n and j == m
        """

