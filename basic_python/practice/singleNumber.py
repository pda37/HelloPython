def singleNumber(nums):
    for i in nums:
        while nums.count(i) == 1:
            return i


print([1, 2, 3, 4, 5, 5, 6, 7])
