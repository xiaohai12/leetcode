class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ## find all solution ----> backtracking
        ret = []
        tmp = []
        self.helper(candidates, tmp, target, ret, 0)
        return ret

    def helper(self, nums, tmp, target, ret, ind):
        if sum(tmp) == target:
            ret.append(tmp.copy())
            return
        if sum(tmp) > target:
            return

        for i in range(ind, len(nums)):
            tmp.append(nums[i])
            self.helper(nums, tmp, target, ret, i)
            tmp.pop()


