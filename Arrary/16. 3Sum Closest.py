class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n <= 2:
            return None
        nums.sort()
        ret = 0
        diff = float('inf')
        for i in range(n - 2):
            if i >= 1 and nums[i - 1] == nums[i]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < diff:
                    ret = s
                    diff = abs(s - target)
                    if diff == 0:
                        return target
                if s < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ret
