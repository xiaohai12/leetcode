class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        #easy way with high complexity
        l = len(nums)
        if l ==1 or nums[0]>nums[1]:
            return 0
        if nums[l-1]>nums[l-2]:
            return l-1
        for i in range(1,l-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        '''
        l = len(nums)
        if l == 1:
            return 0
        return self.helper(0, l - 1, nums)

    def helper(self, low, high, nums):
        if low == high:
            return low
        mid = int((low + high) / 2)
        if nums[mid] < nums[mid + 1]:
            return self.helper(mid + 1, high, nums)
        else:
            return self.helper(low, mid, nums)