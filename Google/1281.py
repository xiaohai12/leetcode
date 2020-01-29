class Solution:
    def subtractProductAndSum(self, n): #: int) -> int:
        strs = str(n)
        Sum = 0
        Prod = 1
        for num in strs:
            num = int(num)
            Prod *=num
            Sum +=num
        return Prod-Sum

if __name__ =='__main__':
    cls = Solution()
    print(cls.subtractProductAndSum(234))