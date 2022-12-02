def maxSubArray(nums):
    currentSubarray = maxSubarray = nums[0]

    for num in nums[1:]:
        currentSubarray = max(num, currentSubarray + num)
        maxSubarray = max(currentSubarray, maxSubarray)
        
    return maxSubarray

maxSubArray([-2,1,-3,4,-1,2,1,-5,4])