def jump(nums):
    n = len(nums) - 1
    a = n
    ans = 0
    while n > 0:
        for i in range(n - 1, max(-1, n - 1001), -1):
            if nums[i] >= n - i:
                a = i
        n = a
        ans += 1
    return ans


print(jump([6, 3, 0, 1, 4]))