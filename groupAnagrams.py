def groupAnagrams(strs):
    res = {}
    for s in strs:
        tmp = list(s)
        tmp.sort()
        S = ''.join(tmp)
        if res.keys()!=None and S in res.keys():
            res[S].append(s)
        else:
            res[S] = [s]
    Res = []
    for key in res.keys():
        Res.append(res[key])
    return Res


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"],))