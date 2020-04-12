class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.findMax(nums, 0, len(nums) - 1)

    def findMax(self, nums, l, h):
        if l == h:
            return l
        mid = int((l + h) / 2)
        left = self.findMax(nums, l, mid)
        right = self.findMax(nums, mid + 1, h)
        if nums[left] > nums[right]:
            return left
        else:
            return right


####### using binary search to find maximun value
####### find maxmun in two list and conbine 