class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        B = nums[::-1]
        A = nums

        for i in range(1, len(nums)):
            if A[i - 1] != 0:
                A[i] *= A[i - 1]
            if B[i - 1] != 0:
                B[i] *= B[i - 1]

        return max(A + B)