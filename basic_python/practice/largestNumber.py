def largestNumber(nums):
    if max(nums) == 0:
        return '0'
    else:
        s = list(str(a) for a in nums)
        print(s)
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[i] + s[j] < s[j] + s[i]:
                    s[i], s[j] = s[j], s[i]
        ans = ''.join(s)
        return ans


print(largestNumber([10, 20]))


# def largestNumber(nums):
#     s = list(str(a) for a in nums)
#     n = len(str(max(nums)))
#     for i in range(len(s)):
#         while len(s[i]) < n:
#             s[i] = s[i] + s[i][0]
#     h = list(int(a) for a in s)
#     sor0 = []
#     sor1 = []
#     for j in range(len(h)):
#         if h[j] == 0:
#             sor1.append(j)
#     while max(h) > 0:
#         ind = h.index(max(h))
#         sor0.append(ind)
#         h[ind] = 0
#     sor0.extend(sor1)
#     ans = ''
#     for k in range(len(sor0)):
#         ans += str(nums[sor0[k]])
#     return ans
