class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set = set([''])
        ret = ''
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word)>len(ret):
                    ret= word
        return ret