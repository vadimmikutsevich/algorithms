def findMaxAverage(nums, k):
    current = answer = 0
    left = 0

    for i in range(k):
        current += nums[i]
        answer = current / k

    for i in range(k, len(nums)):
        current = current - nums[left] + nums[i]  
        if current / k > answer:
            answer = current / k
        left += 1

    print(answer)
    return answer

findMaxAverage([3,3,4,3,0], 3)