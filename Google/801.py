class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        l = len(A)
        if l <= 1:
            return 0
        swap = 1
        fix = 0
        for i in range(1, l):
            if A[i - 1] >= B[i] or B[i - 1] >= A[i]:
                # means we will do same operation as previous
                swap += 1
            elif A[i - 1] >= A[i] or B[i - 1] >= B[i]:
                ## opposite operation as previous
                swap, fix = fix + 1, swap
            else:
                ## even fix or swap is fine
                fix = min(fix, swap)
                swap = fix + 1
        return min(swap, fix)



