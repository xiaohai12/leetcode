class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        low = 0
        high = len(nums)
        mid = 0
        while low < high:
            mid = int((low + high) / 2)
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low
