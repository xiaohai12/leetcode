class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return min(nums)
        l = 0
        r = n - 1
        while l < r:

            if nums[l] < nums[r]:
                return nums[l]

            mid = int((l + r) / 2)
            if mid == l:
                return min(nums[l], nums[r])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]



