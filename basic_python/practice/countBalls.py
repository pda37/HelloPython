def countBalls(lowLimit, highLimit):
    ans = {}
    for i in range(lowLimit, highLimit+1):
        m = 0
        num = str(i)
        for n in num:
            m += int(n)
        if m in ans:
            ans[m] += 1
        else:
            ans[m] = 1
    ans_order = sorted(ans.items(), key=lambda a: a[1], reverse=True)
    return ans_order[0][1]


print(countBalls(5, 15))
