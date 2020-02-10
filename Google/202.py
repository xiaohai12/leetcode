class Solution:
    def isHappy(self, n: int) -> bool:
        ## Floyd Cycle detection algorithm
        slow = n
        fast = n

        while True:
            slow = self.SquareSum(slow)
            fast = self.SquareSum(fast)
            fast = self.SquareSum(fast)
            if fast == slow:
                break
        if slow == 1:
            return True
        else:
            return False

    def SquareSum(self, num):
        s = 0
        for i in str(num):
            s += int(i) ** 2
        return s 