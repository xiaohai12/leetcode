class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=='':
            return True
        if t=='':
            return False
        mat = s[0]
        i = 0
        for char in t:
            if char==mat:
                i +=1
                if i==len(s):
                    return True
                mat = s[i]
        return False