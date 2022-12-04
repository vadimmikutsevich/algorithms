def twoSum(nums, target):
    map = {}

    for i in range(len(nums)):
        map[nums[i]] = i
    for i in range(len(nums)):
        findTarget = target - nums[i]
        if findTarget in map and map[findTarget] != i:
            return [i, map[findTarget]]


twoSum([2,7,11,15], 9)

# we must get two indexes, which can be make a sum of target