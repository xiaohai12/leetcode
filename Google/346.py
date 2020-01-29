class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = size

    def next(self, val: int) -> float:
        if len(self.stack) < self.size:
            self.stack = [val] + self.stack

        else:
            self.stack.pop()
            self.stack = [val] + self.stack
        return (sum(self.stack) / len(self.stack))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)