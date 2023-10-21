def dominantIndex(nums):
    a, b, a_index = 0, 0, 0
    for i in range(len(nums)):
        if nums[i] >= a:
            a, b = nums[i], a
            a_index = i
        elif nums[i] >= b:
            b = nums[i]
    print(a, b)
    if a >= 2*b:
        return a_index
    else:
        return -1


print(dominantIndex([0, 0, 3, 2]))