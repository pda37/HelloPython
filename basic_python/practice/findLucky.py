def findLucky(arr):
    ans = -1
    for a in arr:
        if a == ans:
            continue
        elif arr.count(a) == a:
            ans = max(ans, a)
    return ans


print(findLucky([1, 2, 2, 4]))