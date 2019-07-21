class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        if haystack == '':
            return -1

        l = len(haystack)
        n = len(needle)

        for i in range(l + 1):
            for j in range(n + 1):
                if j == n:
                    return i
                if i + j == l:
                    return -1
                if haystack[i + j] != needle[j]:
                    break