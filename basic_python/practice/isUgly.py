def isUgly(n: int):
    while n > 1 and n % 2 == 0:
        n /= 2
    while n > 1 and n % 3 == 0:
        n /= 3
    while n > 1 and n % 5 == 0:
        n /= 5
    return n == 1


print(isUgly(8))