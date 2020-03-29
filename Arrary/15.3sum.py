class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 2:
            return []

        ret = []
        nums.sort()
        for i in range(n - 2):
            # avoid duplicate
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] < -nums[i]:
                    l += 1

                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1

                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1

        return ret
