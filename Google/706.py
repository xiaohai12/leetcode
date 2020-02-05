class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.index = [None] * self.m

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        ind = key % self.m
        if self.index[ind] == None:
            self.index[ind] = ListNode(key, value)
        else:
            cur = self.index[ind]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        ind = key % self.m
        cur = self.index[ind]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        ind = key % self.m
        prev = cur = self.index[ind]
        if cur == None:
            return

        if cur.pair[0] == key:
            self.index[ind] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


class ListNode:
    def __init__(self, key, value):
        self.pair = (key, value)
        self.next = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)