# 使用缓存通过 动态规划 计算 斐波那契数列 的例子
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(100))


# def fib(n):
#     a, b = 0, 1
#     i = 0
#     while i < n:
#         a, b = b, a+b
#         i += 1
#     return a
#
#
# print(fib(3))
