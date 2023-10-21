# 不使用除法，乘法，mod做除法运算
def divide(dividend, divisor):
    a = abs(dividend)
    b = abs(divisor)
    ans = 0
    while a >= b:
        n = 1
        c = b
        while a >= c >= b:
            a -= c
            ans += n
            c += b
            n += 1
    if divisor * dividend > 0:
        if ans <= 2147483647:
            return ans
        else:
            return 2147483647
    else:
        ans = -ans
        if -2147483648 <= ans:
            return ans
        else:
            return 2147483647


print(divide(-2147483649, 1), -2147483648/1)
print(2**31)
