class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def Sort(item):
            return item[0]

        if intervals == []:
            return []
        intervals.sort(key=Sort)
        ret = []
        start = intervals[0][0]
        end = intervals[0][1]
        for item in intervals:
            if item[0] <= end:
                end = max(item[1], end)
            else:
                ret.append([start, end])
                start = item[0]
                end = item[1]

        ret.append([start, end])
        return ret

