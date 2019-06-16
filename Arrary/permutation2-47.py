class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        per = []
        nums.sort()
        index_list = []
        self.backtrack(nums, ret, per, len(nums), index_list)
        return ret

    def backtrack(self, nums, ret, per, l, index_list):
        if len(per) == l:  # and per.copy() not in ret:
            ret.append(per.copy())
        else:
            for i in range(l):
                if i not in index_list:
                    ## it is important to think about the condition item.
                    if (i > 0) and (nums[i] == nums[i - 1]) and (i - 1 in index_list): continue
                    per.append(nums[i])
                    index_list.append(i)
                    self.backtrack(nums, ret, per, l, index_list)
                    per.pop()
                    index_list.pop()
