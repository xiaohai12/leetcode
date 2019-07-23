class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:
            return []
        l = len(nums)
        nums.sort()
        ret = []
        for i in range(l-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = l-1
            while left<right:
                if nums[left]+nums[right]<-nums[i]:
                    left+=1
                elif nums[left]+nums[right]>-nums[i]:
                    right -=1
                else:
                    ret.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left+1]==nums[left]:
                        left+=1
                    while right>left and nums[right-1]==nums[right]:
                        right -=1
                    left+=1
                    right-=1
                    continue
        return ret 