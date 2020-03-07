class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if source=='' or target=='':
            return -1
        n = len(target)
        m = len(source)
        cur = 0
        s = 0
        while (cur<n):
            tmp = cur
            for i in range(m):
                if cur<n and source[i]==target[cur]:
                    cur +=1
            if tmp==cur:
                return -1
            s+=1
        return s