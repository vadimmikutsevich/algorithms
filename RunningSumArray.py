def runningSum(nums):
    currentSum = nums[0]
        
    for i in range(1, len(nums)):
        currentSum += nums[i]
        nums[i] = currentSum

    print(nums)     
    return nums

runningSum([1,1,1,1,1])