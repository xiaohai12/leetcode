class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Hit = [0] * 300
        self.time = [0] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        ind = timestamp % 300
        if self.time[ind] != timestamp:
            self.time[ind] = timestamp
            self.Hit[ind] = 1
        else:
            self.Hit[ind] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        c = 0
        for i in range(300):
            if timestamp - self.time[i] < 300:
                c += self.Hit[i]
        return c

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)