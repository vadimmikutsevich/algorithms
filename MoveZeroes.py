def moveZeroes(nums):
    l = 0

    for i in range(len(nums)):
        if nums[i]:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1

    print(nums)

moveZeroes([1,0,0,3,12])

# response must be [1,3,12,0,0]