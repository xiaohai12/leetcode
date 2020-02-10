class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ## learn how to use bitwise

        c = 0
        for i in s:
            c ^= ord(i)
        for j in t:
            c ^= ord(j)
        return chr(c)

        # s_dict = {}
        # t_dict = {}
        # for i in s:
        #     c = s_dict.get(i,0)
        #     s_dict[i] = c+1
        # for i in t:
        #     c = t_dict.get(i,0)
        #     t_dict[i] = c+1
        # for key in t_dict.keys():
        #     if key not in s_dict.keys():
        #         return key
        #     elif s_dict[key]!=t_dict[key]:
        #         return key
