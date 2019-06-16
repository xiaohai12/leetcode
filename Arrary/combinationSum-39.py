class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        temp = []
        candidates.sort()
        self.backtrack(candidates, ret, temp, target, 0)
        return ret

    def backtrack(self, nums, ret, temp, target, ind):# ind is used to avoid repeat number
        if target == 0:
            ret.append(temp.copy())
        else:
            for i in range(ind, len(nums)):
                if target < nums[i]:
                    break
                target -= nums[i]
                temp.append(nums[i])
                self.backtrack(nums, ret, temp, target, i)
                temp.pop()
                target += nums[i]
