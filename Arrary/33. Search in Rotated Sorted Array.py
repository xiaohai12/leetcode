class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if nums == []:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = int((l + r) / 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        ro = r
        print(ro)
        if target > nums[-1]:
            r = ro - 1
            l = 0
        elif target < nums[-1]:
            l = ro
            r = len(nums) - 1
        else:
            return len(nums) - 1

        while l <= r:
            mid = int((r + l) / 2)
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1 