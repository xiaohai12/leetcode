class Solution:
    def canWin(self, s: str) -> bool:
        if len(s) < 2:
            return False
        Map = {}
        return self.helper(s, Map)

    def helper(self, s, Map):

        if s in Map.keys():
            return Map[s]

        if "++" not in s:
            Map[s] = False
            return False

        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':
                opp = s[:i] + "--" + s[i + 2:]
                if not self.helper(opp, Map):
                    Map[s] = True
                    return True
        Map[s] = False
        return False

