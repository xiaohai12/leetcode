class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # first solution by DP 
        '''
        dp = [False for i in range(len(s)+1)]
        dp[0]= True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break 
        return dp[-1]

        '''
        # second for bfs
        valid = set([0])
        queue = [0]
        while len(queue) > 0:
            cur = queue.pop()
            for i in range(cur, len(s) + 1):
                if i in valid:
                    continue
                if s[cur:i] in wordDict:
                    if i == len(s):
                        return True
                    queue = [i] + queue
                    valid.add(i)
        return False 



