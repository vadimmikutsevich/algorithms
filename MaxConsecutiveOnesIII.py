def longestOnes(nums, k):
    left = 0

    for right in range(len(nums)):
        if not nums[right]:
            k -= 1

        if k < 0:
            k += 1 - nums[left]
            left += 1

    print(right - left + 1)
    return right - left + 1
        

longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)