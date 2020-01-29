class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if len(A) <= 1:
            return 0
        left = 0
        right = len(A) - 1
        mid = int((left + right) / 2)
        while left < right:
            if A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid
            mid = int((left + right) / 2)
        return left
