class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        S = n
        if S==1:
            return True
        if S<=0:
            return False 
        count =0
        while S!=1:
            S = 0
            N = str(n)
            for string in N:
                S += int(string)**2
            n = S
            count +=1
            if count==10:
                return False 
        return True
        """
        fast = n
        slow = n
        while True:
            slow = self.digitSquareSum(slow)
            fast = self.digitSquareSum(fast)
            fast = self.digitSquareSum(fast)
            if fast==1:
                return True
            if fast==slow:
                return False

    # cycle detection algorithm
    def digitSquareSum(self,num):
        Sum= 0
        while num!=0:
            tmp = num % 10
            Sum += tmp*tmp
            num = num/10
        return Sum
