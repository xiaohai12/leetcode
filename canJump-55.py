def canJump(nums):
    n = len(nums)
    if n == 0:
        return False
    if n == 1:
        return True
    Max = 0
    for i in range(n - 1):
        Max = max(Max, nums[i] + i)
        if Max <= i:
            return False
    return True


print(canJump([3,2,2,0,4]))