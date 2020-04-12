class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        ## dp
        pre = [[]]
        now = [[]]
        for i in range(1,len(nums)+1):
            now = pre.copy()
            for item in pre:
                now.append(item+[nums[i-1]])
            pre = now.copy()
        return now

        '''

        ## recurrent
        l = len(nums)
        if l == 1:
            return [[], nums]
        pre = self.subsets(nums[:-1])
        ret = []
        for item in pre:
            ret.append(item)
            ret.append(item + [nums[-1]])
        return ret
