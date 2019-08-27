class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        for i in range(len(word)):
            try:
                self.list[word[:i + 1]].append(word)
            except:
                self.list[word[:i + 1]] = [word]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.list.keys() and word in self.list[word]:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if prefix in self.list.keys():
            return True
        return False

    # Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)