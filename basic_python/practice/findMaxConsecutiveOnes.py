def findMaxConsecutiveOnes(nums):
    ans = []
    nums1 = list(str(n) for n in nums)
    nums2 = ''.join(nums1)
    nums3 = nums2.split('0')
    for num in nums3:
        ans.append(len(num))
    return max(ans)


print(findMaxConsecutiveOnes([1,1,0,1,1,1]))