class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        start = 0
        end = len(numbers) - 1
        while start < end:
            v = numbers[start] + numbers[end]
            if v == target:
                return [start + 1, end + 1]
            elif v < target:
                start += 1
            else:
                end -= 1
        return []
