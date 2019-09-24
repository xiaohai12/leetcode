class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Map1 = {}
        Map2 = {}
        flag = True
        for i in range(len(s)):
            flag1 = self.check(s[i], t[i], Map1)
            flag2 = self.check(t[i], s[i], Map2)
            if not (flag and flag1 and flag2):
                return False
        return True

    def check(self, s, t, Map):
        if s not in Map.keys():
            Map[s] = t
            return True
        elif Map[s] != t:
            return False
        else:
            return True