class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num
        ## find the 1 in diff
        m = diff & -diff

        ret = [0, 0]
        for num in nums:
            if num & m == 0:
                ret[0] ^= num
            else:
                ret[1] ^= num
        return ret

        '''
        Let a and b be the two unique numbers
        XORing all numbers gets you (a xor b)
        (a xor b) must be non-zero otherwise they are equal
        If bit_i in (a xor b) is 1, bit_i at a and b are different.
        Find bit_i using the low bit formula m & -m
        Partition the numbers into two groups: one group with bit_i == 1 and the other group with bit_i == 0.
        a is in one group and b is in the other.
        a is the only single number in its group.
        b is also the only single number in its group.
        XORing all numbers in a's group to get a
        XORing all numbers in b's group to get b
        Alternatively, XOR (a xor b) with a gets you b.

        '''