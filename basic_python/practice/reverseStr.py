# 反转字符串 II
def reverseStr(s: str, k: int):
    if len(s) < k:
        return s[::-1]
    else:
        n = int(len(s)/k)
        ans = []
        for i in range(n):
            if i % 2 == 0:
                if i == 0:
                    ans.append(s[i * k + k - 1::-1])
                else:
                    ans.append(s[i * k + k-1:i*k-1:-1])
            else:
                ans.append(s[i*k:i*k+k])
        if len(s) % k != 0:
            if n % 2 == 0:
                ans.append(s[:n * k - 1:-1])
            else:
                ans.append(s[n * k:])
        a = ''.join(ans)
        return a


print(reverseStr('ab', 3))
