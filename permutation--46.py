
def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    """
    DP SOLUTION:
    if len(nums)<2:
        return [nums]
    else:
        DP = [[] for i in range(len(nums))]

        for i in range(len(nums)):
            if i ==0:
                DP[i] = [ [x] for x in nums]
            else:
                for dp in DP[i - 1]:
                    for j in nums:
                        if j in dp:
                            continue
                        tmp = dp.copy()
                        tmp.append(j)
                        DP[i].append(tmp)
    return DP[-1]
    """
    res = []
    backtracking(res,  [], nums)
    return res

def backtracking(res, tmp, nums):
    if len(tmp) == len(nums):
        res.append(tmp.copy())
    else:
        for i in range(0,len(nums)):
            if nums[i] in tmp:
                continue
            else:
                tmp.append(nums[i])
            backtracking(res, tmp,nums)
            tmp.pop()


s = permute([1,2,3])
print(s)







