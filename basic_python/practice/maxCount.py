def maxCount(m: int, n: int, ops):
    if ops:
        a = ops[0][0]
        b = ops[0][1]
        for i in range(len(ops)):
            a = min(a, ops[i][0])
            b = min(b, ops[i][1])
        return a * b
    else:
        return m * n


print(maxCount(m=3, n=2, ops=[[2,2],[3,3]]))
