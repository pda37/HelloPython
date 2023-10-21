def isPowerOfFour(n: int):
    while n > 1:
        n /= 4
    return n == 1


print(isPowerOfFour(16))