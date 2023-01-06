def countElements(arr):
    nums_set = set(arr)
    count = 0

    for i in range(len(arr)):
        if arr[i] + 1 in nums_set:
            count += 1
    return count

countElements([1,2,3,3,5])