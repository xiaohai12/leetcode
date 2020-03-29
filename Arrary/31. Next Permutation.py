class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        flag = False
        for i in range(n - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                flag = True
                break
        if flag:
            ## change from i to n-1
            Min = float('inf')
            for j in range(i + 1, n):
                if nums[j] > nums[i] and nums[j] < Min:
                    change = j
            nums[change], nums[i] = nums[i], nums[change]
            nums[i + 1:] = sorted(nums[i + 1:])
        else:
            nums.sort()








