def canMakeArithmeticProgression(nums):
    nums.sort()
    difference = nums[1] - nums[0]
    j = 1

    for i in range(len(nums)):
        if j > len(nums) - 1:
            break
        if nums[j] - nums[i] != difference: return False
        j +=1

    return True

print(canMakeArithmeticProgression([3,5,1]))