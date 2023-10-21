def missingNumber(nums):
    n = len(nums)
    return int((n+1)*n/2 - sum(nums))


print(missingNumber([0, 1]))