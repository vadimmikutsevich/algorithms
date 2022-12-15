def removeDuplicates(nums):
    k = 0
    s = nums[0] - 1

    for i in range(len(nums)):
        if nums[i] != s and nums[i] > s:
            nums[k] = nums[i]
            k += 1
            s = nums[i]
        else:
            nums[i] = '_'

    return k
    



removeDuplicates([1,2,2])

# we expect [1, 2, '_']