class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == []:
            return 0
        left = 0
        right = len(citations) - 1
        l = right + 1
        while left <= right:
            mid = int((left + right) / 2)
            if citations[mid] < l - mid:
                left = mid + 1
            elif citations[mid] == l - mid:
                return citations[mid]
            else:
                right = mid - 1
        return l - left

