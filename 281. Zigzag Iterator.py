class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.iter = []
        n = min(len(v1), len(v2))
        for i in range(n):
            self.iter.append(v1[i])
            self.iter.append(v2[i])
        self.iter += v1[n:] + v2[n:]
        self.ind = -1

    def next(self) -> int:
        if self.ind == len(self.iter) - 1:
            return None

        self.ind += 1
        return self.iter[self.ind]

    def hasNext(self) -> bool:
        return self.ind != len(self.iter) - 1
