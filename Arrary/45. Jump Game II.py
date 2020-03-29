class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        jump = 0
        curEnd = 0
        curFarthest = 0
        for i in range(l-1):
            curFarthest= max(curFarthest,i+nums[i])
            if i==curEnd:
                jump+=1
                curEnd = curFarthest
        return jump