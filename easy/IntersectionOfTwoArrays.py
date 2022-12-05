def intersect(nums1, nums2):
    hash = {}
    result = []

    for i in range(len(nums1)):
        if nums1[i] in hash:
            hash[nums1[i]] = hash[nums1[i]] + 1
        else: 
            hash[nums1[i]] = 1
    
    for i in range(len(nums2)):
        if nums2[i] in hash and hash[nums2[i]] == 1:
            result.append(nums2[i])
            hash.pop(nums2[i])
        elif nums2[i] in hash and hash[nums2[i]] > 1:
            result.append(nums2[i])
            hash[nums2[i]] = hash[nums2[i]] - 1



intersect([4,9,5], [9,4,9,8,4])

# we expect list of elements, which exist in both arrays