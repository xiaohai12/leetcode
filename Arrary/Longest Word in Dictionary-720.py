class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return []
        words.sort()
        ret = ''
        record = set([])
        for word in words:
            if len(word)==1 or word[:-1] in record:
                if len(ret)<len(word):
                    ret = word
                record.add(word)
        return ret