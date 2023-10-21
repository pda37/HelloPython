# 请对输入的数组 就地 进行上述修改，不要从函数返回任何东西
def duplicateZeros(arr):
    k = len(arr)
    d = []
    for i in range(len(arr)):
        if arr[i] == 0:
            d.append(i)
    a = 0
    for j in range(len(d)):
        if d[j]+a < k:
            arr.insert(d[j]+a, 0)
            a += 1
            del arr[-1]
    return arr


print(duplicateZeros([0, 11, 0, 0, 0, 4]))