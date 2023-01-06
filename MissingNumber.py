def missingNumber(nums):
    nums_set = set(nums)
    addNumber = len(nums) + 1

    for i in range(addNumber):
        if i not in nums_set:
            return i

missingNumber([9,6,4,2,3,5,7,0,1])