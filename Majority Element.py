def majorityElement(nums):
    n = 0
    for i in range(0,len(nums)):
        if n == 0:
            major = nums[i]
            n += 1
        elif major == nums[i]:
            n += 1
        else:
            n -=1
            if n ==0:
                major = nums[i]
                n += 1
    return major