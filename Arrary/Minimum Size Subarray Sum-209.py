class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        if s <= 0 or not nums:
            return 0
        Min = float('inf')
        '''
        low = 0 
        Sum = 0


        for i in range(len(nums)):
            Sum +=nums[i]
            while Sum>=s:
                Sum -=nums[low]
                Min = min(Min,i-low+1)
                low +=1
        if Min==float('inf'):
            return 0
        else:
            return Min
        '''
        Sum = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            Sum[i + 1] = Sum[i] + nums[i]
        for i in range(len(nums), -1, -1):
            if Sum[i] >= s:
                low = self.find(Sum, i, s)
                Min = min(i - low + 1, Min)
        if Min == float('inf'):
            return 0
        else:
            return Min

    def find(self, Sum, i, s):
        low = 0
        high = i
        while low <= high:
            mid = int((low + high) / 2)
            if s > Sum[i] - Sum[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low




