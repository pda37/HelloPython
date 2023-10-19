# 两数相加
def addTwoNumbers(l1, l2):
    a1 = 0
    a2 = 0
    for i in range(len(l1)-1, -1, -1):
        a1 = a1 + l1[i]*(10**i)
    for i in range(len(l2)-1, -1, -1):
        a2 = a2 + l2[i]*(10**i)
    a3 = a1 + a2
    b1 = list(int(d) for d in str(a3))  # 整数拆分成列表
    b2 = b1[::-1]
    return b2


r = addTwoNumbers([2, 4, 3], [5, 6, 4])
print(r)