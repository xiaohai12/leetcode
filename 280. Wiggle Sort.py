class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        ## nlogn
        if len(nums)<=1:
            return nums 
        nums.sort()
        l = len(nums)
        for i in range(1,l-1,2):
            nums[i],nums[i+1] = nums[i+1],nums[i]
        return nums

        '''
        ## O(n)
        l = len(nums)
        for i in range(1, l):
            if i % 2 == 1 and nums[i] < nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if i % 2 == 0 and nums[i] > nums[i - 1]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
