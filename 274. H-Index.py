class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        # nlogn
        record = {}
        for num in citations:
            record[num] = record.get(num,0)+1
        tmp = 0
        Max = 0
        for key in sorted(record.keys(),reverse=True):
            record[key] = tmp + record[key]
            tmp =  record[key]
            Max = max(Max,min(tmp,key))
        return Max
        '''
        l = len(citations)
        rec = [0] * l
        for num in citations:
            if num == 0:
                continue
            if num >= l:
                rec[l - 1] += 1
            else:
                rec[num - 1] += 1
        tmp = 0
        Ret = 0
        for i in range(l - 1, -1, -1):
            rec[i] += tmp
            tmp = rec[i]
            Ret = max(Ret, min(i + 1, tmp))
        return Ret
