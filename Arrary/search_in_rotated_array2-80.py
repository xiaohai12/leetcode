class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        if nums == []:
            return False
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return True
            # this is tricky part!! reduce the repeat numbers in left part
            while left < mid and nums[left] == nums[mid]:
                left += 1
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target and target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
