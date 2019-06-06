class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        #solution1
        if k>len(nums):
            k = k%len(nums)
        nums[:] = nums[-k:]+nums[:-k]
        """

        l = len(nums)
        k = k % l
        nums = self.reverse(nums, 0, l - 1)  # reverse from start to end
        nums = self.reverse(nums, 0, k - 1)  # reverse first part
        nums = self.reverse(nums, k, l - 1)  # reverse second part

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return nums