def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    print(nums)
    if len(nums) % 2 == 1:
        return float(nums[int((len(nums)-1)/2)])
    else:
        return float((nums[int(len(nums)/2)]+nums[int(len(nums)/2-1)])/2)


print(findMedianSortedArrays([1], []))