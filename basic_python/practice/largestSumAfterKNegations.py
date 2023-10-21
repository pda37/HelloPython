def largestSumAfterKNegations(nums, k):
    nums.sort()
    max_sum = 0
    for i in range(k):
        if nums[0] >= 0 and (k-i) % 2 == 0:
            break
        else:
            nums[0] = -nums[0]
            nums.sort()
    print(nums)
    for num in nums:
        max_sum += num
    return max_sum


print(largestSumAfterKNegations([-8, 3, -5, -3, -5, -2], 6))