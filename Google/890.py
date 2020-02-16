class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        p_n = set(pattern)
        for word in words:
            if len(set(word))!=len(p_n):
                continue
            dic = {}
            flag = True
            for i,s in enumerate(word):
                if s not in dic.keys():
                    dic[s] = pattern[i]
                elif dic[s]!=pattern[i]:
                    flag=False
            if flag:
                ret.append(word)
        return ret

    '''
    def F(w):
        m = {}
        return [m.setdefault(c,len(m)) for c in w]
    fp = F(patterm)
    return [w for w in words if F(w)==fp]
    '''