class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # this first solution:
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        first = strs[0]
        ret = ""
        for letter in first:
            for i in range(1, len(strs)):
                if strs[i].startswith(ret + letter):
                    continue
                else:
                    return ret
            ret = ret + letter
        return ret