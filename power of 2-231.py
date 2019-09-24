class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        if n==1:
            return True
        while n!=2:
            if not (n&1):
                n>>=1
            else:
                return False
        return True

    '''
    return !(n& (n-1))
    '''