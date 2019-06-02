class Solution:
    def __init__(self,nums):
        self.nums = nums

    def swap(self,A,i,j):
        A[i],A[j] = A[j],A[i]
        return A

    def sortColors(self):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(self.nums)
        second = n-1
        zero = 0
        for i in range(second + 1):
            while self.nums[i] == 2 and i < second:
                self.swap(self.nums, i, second)
                second -= 1
            while self.nums[i] == 0 and i > zero:
                self.swap(self.nums, i, zero)
                zero +=1

nums = [2,0,2,1,1,0]
S = Solution(nums)
S.sortColors()
print(S.nums)
