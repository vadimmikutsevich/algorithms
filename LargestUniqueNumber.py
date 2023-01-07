def largestUniqueNumber(nums):
    hashMap = {}
    repeatedLetters = {}

    for i in range(len(nums)):
        if nums[i] in hashMap:
            hashMap.pop(nums[i])
            repeatedLetters[nums[i]] = i
        elif nums[i] in repeatedLetters:
            repeatedLetters[nums[i]] += 1
        else:
            hashMap[nums[i]] = i
                
    if not hashMap:
        return -1

    result = list(hashMap) if list(hashMap) else -1
    return sorted(result)[len(result) - 1]

largestUniqueNumber([5,7,3,9,4,9,8,3,1])


# Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.