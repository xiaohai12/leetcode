class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[-1]

        result = nums[0]
        for i in range(1, l):
            result ^= nums[i]
        return result
