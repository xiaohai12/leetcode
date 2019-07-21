class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        rec = dict()
        for i in range(len(nums)):
            if target - nums[i] in rec.keys():
                return [rec[target - nums[i]], i]
            rec[nums[i]] = i
        return []
