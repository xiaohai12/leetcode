class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        start = 0
        ## two pointer
        Max = 0
        for i, letter in enumerate(s):
            if letter in used.keys() and start <= used[letter]:
                start = used[letter] + 1
            else:
                Max = max(Max, i - start + 1)

            used[letter] = i
        return Max