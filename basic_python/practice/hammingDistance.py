def hammingDistance(x, y):
    a, b = list(bin(x)[2:]), list(bin(y)[2:])
    ans = 0
    n = min(len(a), len(b))
    for i in range(-1, -n-1, -1):
        if a[i] != b[i]:
            ans += 1
    if len(a) < len(b):
        for i in range(len(b) - n):
            if b[i] == '1':
                ans += 1
    else:
        for i in range(len(a) - n):
            if a[i] == '1':
                ans += 1
    return ans


print(hammingDistance(12, 12))