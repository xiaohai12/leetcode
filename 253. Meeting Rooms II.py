class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []

        for item in intervals:
            start.append(item[0])
            end.append(item[1])
        start.sort()
        end.sort()

        s = e = 0
        room = available = 0
        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    room += 1
                else:
                    available -= 1
                s += 1
            else:
                available += 1
                e += 1
        return room