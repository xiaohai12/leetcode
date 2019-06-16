class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = []
        candidates.sort()
        self.backtrack(candidates, ret, temp, target, 0)
        return ret

    def backtrack(self, nums, ret, temp,target,ind):
        if target == 0:
            ret.append(temp.copy())
        else:
            for i in range(ind, len(nums)):
                if target < nums[i]:
                    break
                if i > ind and nums[i] == nums[i - 1]: #avoid repeat list
                    continue
                target -= nums[i]
                temp.append(nums[i])
                self.backtrack(nums, ret, temp, target, i + 1)
                temp.pop()
                target += nums[i]