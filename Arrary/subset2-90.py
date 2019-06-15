class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        sub = []
        nums.sort()
        self.bfs1(nums, ret, sub, 0)
        return ret

    def bfs(self, nums, ret, sub, index):
        if sub not in ret:
            ret.append(sub.copy())
            l = len(nums)
            for i in range(index, l):
                sub.append(nums[i])
                self.bfs(nums, ret, sub, i + 1)
                sub.pop()

    def bfs1(self, nums, ret, sub, index):
        ret.append(sub.copy())
        l = len(nums)
        for i in range(index, l):
            if (i > index and nums[i] == nums[i - 1]): continue  # skip the branch
            sub.append(nums[i])
            self.bfs1(nums, ret, sub, i + 1)
            sub.pop()
