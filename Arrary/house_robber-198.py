class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 1:
            return sum(nums)
        DP = [0 for i in range(len(nums))]
        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            DP[i] = max(DP[i - 1], DP[i - 2] + nums[i])
        return DP[-1]
