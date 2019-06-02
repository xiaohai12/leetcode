# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        elif len(intervals) == 1:
            return intervals

        else:
            intervals.sort(key=self.sortedkey)
            res = [intervals[0]]
            for elem in intervals:
                flag = False
                for ind, e in enumerate(res):
                    if elem.start >= e.start and elem.start <= e.end:
                        e.end = max(e.end, elem.end)
                        flag = True
                    else:
                        continue
                if flag == False:
                    res.append(elem)
            return res

    def sortedkey(self, elem):
        return elem.start