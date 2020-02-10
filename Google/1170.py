class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_f = [word.count(min(word)) for word in words]
        l = len(words)
        m = [0] * 11
        biggerthan = [0] * 11
        for f in words_f:
            m[f] += 1
        for i in range(1, 11):
            m[i] += m[i - 1]
            biggerthan[i] = l - m[i]
        return [biggerthan[i.count(min(i))] for i in queries]

