class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ret = {}
        for i in s:
            if i in ret.keys():
                del ret[i]
            else:
                ret[i] = 1
        if len(ret.keys())<=1:
            return True
        return False