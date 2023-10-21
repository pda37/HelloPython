import math
def primeNumberArrangement(n):
    composite_number = []
    prime_number = list(k for k in range(1, n+1))
    # print(prime_number)
    for i in range(3, n+1):
        for j in range(2, math.ceil(math.sqrt(i))+1):
            if i % j == 0:
                composite_number.append(i)
                break
    # print(composite_number)
    for num in composite_number:
        prime_number.remove(num)
    return prime_number


print(primeNumberArrangement(100000))