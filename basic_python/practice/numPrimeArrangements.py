import math
def numPrimeArrangements(n: int):
    non_prime = 1
    for i in range(3, n+1):
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                non_prime += 1
                break
    ans = 1
    for i in range(1, non_prime+1):
        ans *= i
    for i in range(1, n - non_prime + 1):
        ans *= i
    return ans % (10**9+7)


print(numPrimeArrangements(100))