def minMoves(nums):
    ans = 0
    m = min(nums)
    for num in nums:
        ans += num - m
    return ans


print(minMoves([1, 2, 3]))
