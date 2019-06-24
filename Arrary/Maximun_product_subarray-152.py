class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        Max = nums[0]
        Min = nums[0]
        r = Max
        for i in range(1,len(nums)):
            if nums[i]<0:
                tmp = Max
                Max =Min
                Min = tmp
            Max = max(nums[i],nums[i]*Max)
            Min = min(nums[i],nums[i]*Min)
            ## try to understand this two line
            ##        // max/min product for the current number is either the current number itself
        # or the max/min by the previous number times the current one
            r = max(r,Max)
        return r