def removeElement(nums, val):
    k = 0
    n = len(nums)

    while k < n:
        if nums[k] == val:
            nums[k] = nums[n - 1]
            n -= 1
        else:
            k += 1

    return k

removeElement([5,2,4,7,1,4,7,8,3], 4)

# we expect [5, 2, 3, 7, 1, 8, 7, 8, 3]