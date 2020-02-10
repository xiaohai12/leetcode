class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        Sum = []
        s = 0
        for num in nums:
            s +=num
            Sum.append(s)
        Min = 0
        large = nums[0]
        for s in Sum:
            large = max(large,s-Min)
            Min = min(s,Min)
        return large