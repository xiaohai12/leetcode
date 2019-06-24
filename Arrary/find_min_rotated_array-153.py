class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[-1]
        left = 0
        right = l - 1
        Min = nums[0]
        while left <= right:
            mid = int((left + right) / 2)
            Min = min(Min, nums[left])
            if nums[left] > nums[mid]:
                right = mid
            else if nums:
                left = mid + 1
        return Min
