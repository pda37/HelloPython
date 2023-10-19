def findMaxAverage(nums, k):
    win = sum(nums[0:k])
    ans = [win]
    for i in range(len(nums)-k):
        win = win - nums[i] + nums[i+k]
        ans.append(win)
    return max(ans)/k


print(findMaxAverage([1,12,-5,-6,50,3], 4))
