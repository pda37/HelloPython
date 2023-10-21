def findComplement(num):
    ans = list(int(a) for a in bin(num)[2:])
    ans_complement = list(map(lambda x: 1-x, ans))
    a = 0
    n = len(ans_complement)
    for i in range(n):
        a += ans_complement[i]*(2**(n - i - 1))
    return a


print(findComplement(1))