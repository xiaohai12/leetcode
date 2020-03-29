class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## repeat three times so that we have three stage
        ## we can use two bits to represent them 00-->01-->10-->00
        one = 0  # first bit
        two = 0  # second bit
        for num in nums:
            one = one ^ num & (~two)  ## if num show first time, it will == one
            two = two ^ num & (~one)  ## if num show second time it will == two
            print(one, two)
        return one

