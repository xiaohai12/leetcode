class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        c = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] >= target - nums[i]:
                    right -= 1
                else:
                    c += right - left
                    left += 1
        return c

