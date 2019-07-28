class Solution:
    def partition(self, s: str) -> List[List[str]]:

        l = len(s)
        if s == 0:
            return []
        if s == 1:
            return [[s]]
        '''
        #DP version :
        dp = [[] for i in range(l+1)]
        dp[0]=[]
        dp[1] = [[s[0]]]
        for i in range(2,l+1):
            for start in range(0,i):
                if self.check(s,start,i-1):
                    if start==0:
                        dp[i].append([s[start:i]])
                    else:
                        for item in dp[start]:
                            dp[i].append(item+[s[start:i]])
        return dp[-1]
        '''

        # DFS version:
        ret = []
        tmp = []
        self.helper(s, 0, tmp, ret)
        return ret

    def helper(self, s, ind, tmp, ret):
        if len(s) == ind:
            ret.append(tmp.copy())
            return
        for i in range(ind, len(s)):
            if self.check(s, ind, i):
                tmp.append(s[ind:i + 1])
                self.helper(s, i + 1, tmp, ret)
                tmp.pop()

    def check(self, s, start, end):
        if end == start:
            return True

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

