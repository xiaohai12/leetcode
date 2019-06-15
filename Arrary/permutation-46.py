class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        per = []
        nums.sort()
        self.backtrack(nums, ret, per, len(nums))
        return ret

    def backtrack(self, nums, ret, per, l):
        if len(per) == l:
            ret.append(per.copy())
        else:
            for i in range(len(nums)):
                if nums[i] not in per:
                    per.append(nums[i])
                    self.backtrack(nums, ret, per, l)
                    per.pop()
                else:
                    continue