class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == '' or words == []:
            return []

        dic = {}
        for word in words:
            dic[word] = dic.get(word, 0) + 1
        ret = []
        l = len(words[0])
        n = len(words)
        for i in range(0, len(s) - n * l + 1):
            seen = {}
            j = 0
            while j < n:
                w = s[i + j * l:i + l * j + l]
                if w in dic.keys():
                    seen[w] = seen.get(w, 0) + 1
                    if seen[w] > dic[w]:
                        break
                    j += 1
                else:
                    break
            if j == n:
                ret.append(i)
        return ret
