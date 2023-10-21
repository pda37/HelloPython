def totalMoney(n: int) -> int:
    a = int(n / 7)
    b = n % 7
    print(a, b)
    ans = 0
    for i in range(1, a+1):
        for j in range(i, i+7):
            ans += j
    for k in range(1, b+1):
        ans += a+k
    return ans


print(totalMoney(10))