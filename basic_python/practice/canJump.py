def canJump(nums):
    if nums[0] == 0 and len(nums) > 1:
        return False
    else:
        n = 0
        for i in range(len(nums)-2, 0, -1):
            if nums[i] == 0:
                for j in range(0, i):
                    if nums[j] > i - j:
                        n = 0
                        print(n)
                        break
                    else:
                        n += 1
                if n == i:
                    return False
        return True


print(canJump([2, 0, 0]))