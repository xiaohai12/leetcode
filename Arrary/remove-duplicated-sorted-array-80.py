def removeDuplicates(nums,k):
    # set a another index as loc to record the index that should be change to another value
    # two indexes (i and j) go together at first
    i = k
    for j in range(k,len(nums)):
        if nums[j] > nums[i-k]:
            nums[i] = nums[j]
            i += 1
    return i


nums = [0,1,1,1,2,2,3,3,3]
a = removeDuplicates(nums,2)
print(a)