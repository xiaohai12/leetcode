class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if strs == []:
            return []

        rec = {}
        for Str in strs:
            key = tuple(sorted(Str))
            rec[key] = rec.get(key, []) + [Str]
        return list(rec.values())
