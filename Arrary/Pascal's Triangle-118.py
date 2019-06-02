class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        dp = [[[]] for i in range(numRows)]
        dp[0] = [[1]]
        for i in range(1,numRows):
            dp[i]=dp[i-1]
            add = [0 for x in range(i+1)]
            add[0]=1
            add[-1]=1
            for j in range(1,i):
                add[j] = dp[i-1][-1][j-1]+dp[i-1][-1][j]
            dp[i].append(add)
        return dp[numRows-1]
    '''
    # best solution:
    res = [[1]]
    for i in range(1, numRows):
        res += [list(map(lambda x, y: x + y, [0] + res[-1], res[-1] + [0]))]
    return res[:numRows]
    
    # solution 2:
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
    
    
    # comment:
    1).learn how to use map function
    2).rule: 1,3,3,1  next one can be  [0,1,3,3,1]+[1,3,3,1,0]
    ’‘’