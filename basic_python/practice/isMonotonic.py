# 单调数列
def isMonotonic(nums):
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        return True
    return False


print(isMonotonic([1, 4, 3, 3, 5]))