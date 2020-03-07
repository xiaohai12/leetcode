class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        first = A[0]
        second = B[0]

        def count(A, B, ref):
            c1 = 0
            c2 = 0
            for i in range(len(A)):
                if A[i] != ref and B[i] != ref:
                    return -1
                if A[i] != ref:
                    c1 += 1
                if B[i] != ref:
                    c2 += 1
            return min(c1, c2)

        f1 = count(A, B, first)
        s1 = count(A, B, second)

        ret = min(f1, s1)
        re = max(f1, s1)
        return ret if ret != -1 else re
