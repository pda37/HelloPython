def isPerfectSquare(num):
    a = 1
    b = num / a
    while a < b:
        a += 1
        b = num / a
    return a == b


print(isPerfectSquare(20000))
