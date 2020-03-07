class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        Dis = {}
        ret = [0] * len(workers)
        flag_w = [False] * len(workers)
        flag_b = [False] * len(bikes)
        for w, worker in enumerate(workers):
            for b, bike in enumerate(bikes):
                dis = abs(bike[0] - worker[0]) + abs(bike[1] - worker[1])
                if dis not in Dis.keys():
                    Dis[dis] = [(w, b)]
                else:
                    Dis[dis].append((w, b))

        for key in sorted(Dis.keys()):
            for (w, b) in Dis[key]:
                if not flag_w[w] and not flag_b[b]:
                    ret[w] = b
                    flag_w[w] = True
                    flag_b[b] = True
        return ret
