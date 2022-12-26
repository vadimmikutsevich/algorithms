def rotate(nums, k):
    k = k % len(nums)

    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    print(nums)

rotate([3,2], 3)

# k is num of elems, which we need to move to the start of the array