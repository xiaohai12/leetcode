class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.i = 0
        self.list = []
        for item in v:
            self.list += item

    def next(self) -> int:
        self.i += 1
        return self.list[self.i - 1]

    def hasNext(self) -> bool:
        return self.i < len(self.list)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()