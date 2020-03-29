class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]

        ## find the leftmost and rightmost number

        l = 0
        r = len(nums) - 1
        leftmost = float('inf')
        while l <= r:
            mid = int((r + l) / 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                leftmost = min(leftmost, mid)
                r = mid - 1
        l = 0
        r = len(nums) - 1
        rightmost = -float('inf')
        while l <= r:
            mid = int((r + l) / 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                rightmost = max(rightmost, mid)
                l = mid + 1

        if rightmost == -float('inf'):
            return [-1, -1]
        return [leftmost, rightmost]


