class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        visted = set(deadends)
        q = deque(['0000'])
        depth = -1
        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node in visted:
                    continue
                if node == target:
                    return depth
                visted.add(node)
                q.extend(self.neighbor(node))
        return -1

    def neighbor(self, node):
        ret = []
        for i, s in enumerate(node):
            c = int(s)
            ret.append(node[:i] + str((c + 1) % 10) + node[i + 1:])
            ret.append(node[:i] + str((c - 1) % 10) + node[i + 1:])
        return ret