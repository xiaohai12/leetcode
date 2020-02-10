class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 10000
        self.m = 1000

    def add(self, key: int) -> None:
        ind = key % self.m
        div = int(key / self.m)
        if self.table[ind] == None:
            self.table[ind] = [False] * 1000
        self.table[ind][div] = True

    def remove(self, key: int) -> None:
        ind = key % self.m
        div = int(key / self.m)
        if self.table[ind] != None:
            self.table[ind][div] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        ind = key % self.m
        div = int(key / self.m)
        if self.table[ind] != None:
            return self.table[ind][div]
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)