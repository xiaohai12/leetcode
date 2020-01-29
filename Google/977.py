class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if len(A)<=1:
            return [s**2 for s in A]
        left = []
        right = []
        for num in A:
            if num<=0:
                left.append(num)
            else:
                right.append(num)
        ret = []
        i = len(left)-1
        j = 0
        while i>=0 and j <len(right):
            l = left[i]**2
            r = right[j]**2
            if l<=r:
                ret.append(l)
                i -=1
            else:
                ret.append(r)
                j +=1
        return ret+[left[i]**2 for i in range(i,-1,-1)]+[s**2 for s in right[j:]]