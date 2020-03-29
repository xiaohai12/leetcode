class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        tmp = []
        candidates.sort()
        self.helper(candidates, target, tmp, ret, 0)

        return ret

    def helper(self, nums, target, tmp, ret, ind):
        if target == 0:
            ret.append(tmp.copy())
            return

        if target < 0:
            return

        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue  ## this is used to avoid duplicated items !!!!!!!!!!!!!!!!!
            target -= nums[i]
            tmp.append(nums[i])
            self.helper(nums, target, tmp, ret, i + 1)
            tmp.pop()
            target += nums[i]
