class DoubleLink:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.Next = None
        self.Pre = None


class LRUCache(object):

    ## fast lookup: hashtable
    ## fast removal: doubled linklist

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dhead = DoubleLink(0, 0)
        self.dtail = DoubleLink(0, 0)
        self.dhead.Next = self.dtail
        self.dtail.Pre = self.dhead
        self.capacity = capacity
        self.cache = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache.keys():
            tmp = self.cache[key]
            self.remove(tmp)
            self.add(tmp)
            return tmp.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache.keys():
            self.remove(self.cache[key])
        new = DoubleLink(value, key)
        self.add(new)
        self.cache[key] = new
        if len(self.cache.keys()) > self.capacity:
            dele = self.dtail.Pre
            self.remove(dele)
            del self.cache[dele.key]

    def remove(self, link):
        p = link.Pre
        n = link.Next
        p.Next = n
        n.Pre = p

    def add(self, link):
        n = self.dhead.Next
        n.Pre = link
        link.Next = n
        link.Pre = self.dhead
        self.dhead.Next = link

    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)