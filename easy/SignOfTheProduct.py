def arraySign(nums):
    count = nums[0]
    j = 1

    for i in range(len(nums)):
        if j > len(nums) - 1:
            break

        count *= nums[j]
        j += 1

    if count < 0: return -1
    if count > 0: return 1
    if count == 0: return 0
   

print(arraySign([-1,-2,-3,-4,3,2,1]))

# we expect:
#   1 if the product is positive
#   -1 if the product is negative
#   0 if the product is equal to 0