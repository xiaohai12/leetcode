def subsets(nums):
    '''
    # DP method
    l = len(nums)
    if l <= 1:
        return [nums] + [[]]
    dp = [[] for i in range(l)]
    dp[0] = [[x] for x in nums]
    ret = [[]] + dp[0]
    for i in range(1, l):
        for elem in dp[i - 1]:
            for num in nums:
                temp = elem.copy()
                if num not in temp:
                    temp.append(num)
                else:
                    continue
                temp.sort()
                if temp not in dp[i]:
                    dp[i].append(temp)
        ret += dp[i]
    return ret
    '''
    sub = []
    ret = []
    nums.sort()
    backtrack(nums, ret, sub, 0)
    return ret


def backtrack(nums, ret, sub, index):
    ret.append(sub.copy())
    l = len(nums)
    for i in range(index, l):
        sub.append(nums[i])
        print(i, '  ', sub)
        backtrack(nums, ret, sub, i + 1) ## bfs nums[i+1:]
        sub.pop()

