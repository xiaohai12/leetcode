class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):

        self.rec = {}
        self.dictionary = set(dictionary)
        for word in dictionary:
            abb = self.abbreviation(word)
            if len(abb) > 2:
                self.rec[abb] = self.rec.get(abb, 0) + 1

    def isUnique(self, word: str) -> bool:
        abb = self.abbreviation(word)
        if len(abb) > 2:
            if word not in self.dictionary:
                if abb in self.rec.keys():
                    return False
            else:
                if self.rec[abb] >= 2:
                    return False
        return True

    def abbreviation(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)