def getPermutation(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    mul = 1
    nums = []
    for i in range(1, n + 1):
        mul *= i
        nums.append(str(i))
    s = ''
    step = n
    k -= 1
    while k != 0:
        mul = int(mul / step)
        ind = int(k / mul)
        step -= 1
        k = k % mul
        s += nums[ind]
        nums.remove(nums[ind])
    left = ''.join(nums)
    s += left
    return s