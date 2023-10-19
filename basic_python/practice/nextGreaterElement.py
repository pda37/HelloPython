def nextGreaterElement(nums1, nums2):
    ans = []
    for num in nums1:
        a = 0
        for i in range(nums2.index(num), len(nums2)):
            if nums2[i] > num:
                ans.append(nums2[i])
                a = 1
                break
        if a == 0:
            ans.append(-1)
    return ans


print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))