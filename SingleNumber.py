def singleNumber(nums):
    hashMap = {}

    for i in range(len(nums)):
        if nums[i] in hashMap:
            hashMap.pop(nums[i])
        else: 
            hashMap[nums[i]] = i

    return list(hashMap.keys())[0]

singleNumber([4,1,2,1,2])

# we expect to see single number among double numbers in array