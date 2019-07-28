class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 0 or k == 0 or k > n:
            return []
        ret = []
        temp = []
        self.helper(n, k, ret, temp, 1)
        return ret

    def helper(self, n, k, ret, temp, ind):
        if len(temp) == k:
            ret.append(temp.copy())
            return

        for i in range(ind, n + 1):
            temp.append(i)
            self.helper(n, k, ret, temp, i + 1)
            temp.pop()
