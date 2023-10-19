def findDisappearedNumbers(nums):
    ans = []
    n = len(nums)
    num = set(nums)
    for i in range(1, n+1):
        if i not in num:
            ans.append(i)
    return ans


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))