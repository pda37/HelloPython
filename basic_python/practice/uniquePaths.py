def uniquePaths(m, n):
    ans = 1
    if m > n:
        # 一共要向右走m-1步，向下走n-1步，共m+n-2步
        # 共有多少走的方法，看作是在m+n-2步中选择n-1步
        for i in range(n-1):
            ans *= m+i
            ans /= n-1-i
        return round(ans, 0)
    else:
        for i in range(m-1):
            ans *= n+i
            ans /= m-1-i
        return round(ans)


print(uniquePaths(10, 10))