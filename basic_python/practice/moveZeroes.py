def moveZeroes(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
    return nums


print(moveZeroes([0, 0, 0]))