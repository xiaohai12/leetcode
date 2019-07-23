class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l < 2:
            return s
        store = {}
        for i in range(0, l):
            l1, r1 = self.checkPalindromic(s, i, i)
            l2, r2 = self.checkPalindromic(s, i, i + 1)
            store[r1 - l1 + 1] = (l1, r1)
            store[r2 - l2 + 1] = (l2, r2)
        (l, r) = store[max(store.keys())]
        print(l, r)
        return s[l:r + 1]

    def checkPalindromic(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return l + 1, r - 1