class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        n = len(words_list)
        if n==0:
            return ''
        s = ''
        for i in range(n-1,-1,-1):
            s += words_list[i]+' '
        return s[:-1]