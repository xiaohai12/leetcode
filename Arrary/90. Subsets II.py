class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                l = len(ret)
            for j in range(len(ret)-l,len(ret)):
                ret.append(ret[j]+[nums[i]])
        return ret