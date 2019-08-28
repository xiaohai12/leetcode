
def rob(nums) -> int:

    return robs(nums,0)

def robs(nums,i):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    if i==0:
        if len(nums) == 3:
            return max(nums)
        s = robs(nums[2:-1],1)
        d = robs(nums[3:],1)
        try:
            k = robs(nums[4:],1)
        except:
            k = 0
        return max(nums[0] + s, nums[1] +d,nums[2]+k)
    else:
        s = robs(nums[2:],1)
        try:
            d = robs(nums[3:],1)
        except:
            d=0
        try:
            k = robs(nums[4:],1)
        except:
            k = 0
        return max(nums[0] + s, nums[1] + d,nums[2]+k)

print(robs([1, 2, 3, 4, 5, 1, 2, 3, 4, 5],0))