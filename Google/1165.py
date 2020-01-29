class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        dic = {}
        for i, letter in enumerate(keyboard):
            dic[letter] = i
        last = 0
        step = 0
        for s in word:
            step += abs(dic[s] - last)
            last = dic[s]
        return step
