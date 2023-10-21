def containsNearbyDuplicate(nums, k):
    ans = {}
    for i in range(len(nums)):
        if nums[i] not in ans:
            ans[nums[i]] = i
        else:
            if abs(i - ans[nums[i]]) <= k:
                return True
            else:
                ans[nums[i]] = i
    return False


print(containsNearbyDuplicate([1,2,3,1], 2))