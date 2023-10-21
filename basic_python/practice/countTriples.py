import math
def countTriples(n: int):
    ans = 0
    for c in range(2, n+1):
        for a in range(1, c):
            b = int(math.sqrt(c**2 - a**2))
            if a**2 + b**2 == c**2:
                ans += 1
    return ans


print(countTriples(10))
