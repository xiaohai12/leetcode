class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        ## O(nlogn):
        if nums == []:
            return 0
        S = [0]
        n = len(nums)
        for i in range(n):
            S.append(S[-1] + nums[i])

        Min = n + 1
        for j in range(n):
            l = j
            r = n
            target = s + S[j]
            while l < r:
                mid = int((l + r) / 2)
                if S[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            if S[l] >= target:
                Min = min(Min, l - j)
        if Min == n + 1:
            return 0
        else:
            return Min

        '''

        ## O(n)
        if nums==[]:
            return 0

        start = 0
        S = 0
        Min  = len(nums)+1
        for i in range(len(nums)):
            S += nums[i]
            while S>=s:
                Min = min(Min,i-start+1)
                S -= nums[start]
                start +=1 
        if Min==len(nums)+1:
            return 0
        else:
            return Min


        '''


