def nextPermutation(nums):
    n = len(nums)
    a = 0
    for i in range(n-1, 0, -1):
        if nums[i-1] < nums[i] and a == 0:
            for j in range(n-1, i-1, -1):
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    print(nums)
                    a += 1
                    s = sorted(nums[i:n])
                    print(s)
                    for k in range(len(s)):
                        nums[i+k] = s[k]
                    break
    print(nums)
    if a == 0:
        for k in range(int(n/2)):
            nums[k], nums[n - 1 - k] = nums[n - 1 - k], nums[k]
    print(nums, a)


print(nextPermutation([1, 2, 3]))
print(nextPermutation([3, 2, 1]))
