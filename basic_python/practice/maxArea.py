# 盛最多水的容器
def maxArea(height):
    a = 0
    i = 0
    j = len(height)-1
    while i < j:
        s = abs((i-j)*(min(height[i], height[j])))
        a = max(a, s)
        if height[i] > height[j]:
            j = j - 1
        else:
            i = i + 1
    return a


r = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(r)