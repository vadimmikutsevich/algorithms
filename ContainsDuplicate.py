def containsDuplicate(nums):
    checkWithSet = set(nums)

    if len(nums) > len(checkWithSet): return true
    else: false

containsDuplicate([1,2,3,1])

# we expect False if there aren't duplicate elems or True if they are