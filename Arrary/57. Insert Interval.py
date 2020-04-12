class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if intervals == []:
            return [newInterval]

        ret = []
        flag = True
        for item in intervals:
            if item[1] < newInterval[0]:
                ret.append(item)

            elif item[0] > newInterval[1]:
                if flag:
                    ret.append(newInterval)
                    flag = False
                ret.append(item)
            else:
                newInterval = [min(item[0], newInterval[0]), max(item[1], newInterval[1])]

        if flag:
            ret.append(newInterval)
        return ret
