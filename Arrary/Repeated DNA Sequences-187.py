class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        if l<10:
            return []
        rec = set()
        ret = set()
        for i in range(l-9):
            key = s[i:i+10]
            if key in rec:
                ret.add(key)
            rec.add(key)
        return list(ret)