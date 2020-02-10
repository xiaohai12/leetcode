class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            c = s_dict.get(i,0)
            s_dict[i] = c+1
        for j in t:
            c = t_dict.get(j,0)
            t_dict[j] = c+1
        return t_dict==s_dict
        