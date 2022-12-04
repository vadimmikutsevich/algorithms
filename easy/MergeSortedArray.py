def merge(nums1, m, nums2, n):
    for i in range(m + n):
        if i < m:
            nums1[i] = nums1[i]
        elif n > 0:
            nums1[i] = nums2[i - m]
    nums1.sort()

merge([1,2,3,0,0,0], 3, [2,5,6], 3)

# we expect [1,2,2,3,5,6] instead of nums1