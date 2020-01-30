class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sort = self.FastSort(heights)
        s = 0
        for i in range(len(heights)):
            if heights_sort[i] != heights[i]:
                s += 1
        return s

    def FastSort(self, nums):
        if len(nums) <= 1:
            return nums
        left = []
        right = []
        head = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if num <= head:
                left.append(num)
            else:
                right.append(num)
        left_sort = self.FastSort(left)
        right_sort = self.FastSort(right)
        return left_sort + [head] + right_sort

    def countingSort(self, nums):
        if len(nums) <= 1:
            return nums
        Max = max(nums)
        Min = min(nums)
        record = [0] * (Max - Min + 1)
        ret = list(range(len(nums)))
        for num in nums:
            record[num - Min] += 1
        for i in range(1, len(record)):
            record[i] += record[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            ret[record[nums[i] - Min] - 1] = nums[i]
            record[nums[i] - Min] -= 1
        return ret
