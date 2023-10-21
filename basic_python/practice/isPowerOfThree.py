def isPowerOfThree(n):
    if n <= 0:
        return False
    elif n == 1:
        return True
    else:
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
            print(n)
        return n == 1


print(isPowerOfThree(45))
