class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        i = 0
        for j in t:
            if s[i] == j:
                i += 1
                if i == len(s):
                    return True
        return False
