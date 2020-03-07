class SnapshotArray:

    def __init__(self, length: int):
        self.data = [0] * length
        self.snapshots = {0: {i: 0 for i in range(length)}}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.data[index] = val
        self.snapshots[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.snapshots[self.snap_id] = {}
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        while index not in self.snapshots[snap_id]:
            snap_id -= 1
        return self.snapshots[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)