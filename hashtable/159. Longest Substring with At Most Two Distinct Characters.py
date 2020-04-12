class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if s == '':
            return 0

        start = 0
        freq = {}
        length = 0
        for i in range(len(s)):
            if s[i] in freq.keys():
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

            while len(freq.keys()) > 2:
                key = s[start]
                start += 1
                freq[key] -= 1
                if freq[key] == 0:
                    del freq[key]
            length = max(length, i - start + 1)
        return length

