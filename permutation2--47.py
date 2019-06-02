def permuteUnique(nums):
    res = []
    used = [False for i in range(len(nums))]
    tmp = []
    nums.sort()
    backtracking(res,used,tmp,nums)
    return res

def backtracking(res,used,tmp,nums):
    if len(tmp)==len(nums):
        res.append(tmp.copy())
    else:
        for i in range(len(nums)):
            if used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1]):
                continue
            else:
                tmp.append(nums[i])
                used[i]=True
            backtracking(res,used,tmp,nums)
            tmp.pop()
            used[i]=False

s= permuteUnique([1,2,1])
print(s)
