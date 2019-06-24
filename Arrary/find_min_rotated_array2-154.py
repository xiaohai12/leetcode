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
            elif nums[left]<nums[mid]:
                left = mid + 1
            else:
                left+=1 ## until we remove the equile!
        return Min