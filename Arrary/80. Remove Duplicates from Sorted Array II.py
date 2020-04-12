class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        '''
        freq = 1
        num = nums[0]
        l = len(nums)
        point = 1
        for i in range(1,l):
            if nums[i]!=num:
                nums[point] = nums[i]
                point +=1 
                freq = 1
                num = nums[i]
            else:
                freq +=1 
                if freq<3:
                    nums[point] = nums[i]
                    point +=1

        return point

        '''
        i = 0
        for num in nums:
            if i < 2 or num > nums[i - 2]:
                nums[i] = num
                i += 1
        return i



