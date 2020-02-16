class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        lenA = len(A)
        lenB = len(B)
        ret = []
        i = 0
        j = 0
        while i < lenA and j < lenB:
            if A[i][1] < B[j][0]:
                i += 1
                continue
            if A[i][0] > B[j][1]:
                j += 1
                continue
            ret.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ret

