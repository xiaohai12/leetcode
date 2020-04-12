class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ret = []
        if nums == []:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]

        if lower == upper:
            return []

        for i in range(len(nums)):

            if nums[i] == lower + 1:
                ret.append(str(lower))

            elif nums[i] > lower + 1:
                ret.append(str(lower) + '->' + str(nums[i] - 1))

            lower = nums[i] + 1

            if i == len(nums) - 1:
                if lower == upper:
                    ret.append(str(lower))
                elif lower < upper:
                    ret.append(str(lower) + '->' + str(upper))

        return ret
