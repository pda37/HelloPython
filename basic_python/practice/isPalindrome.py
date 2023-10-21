import re


def isPalindrome(s):
    # s1 = s.lower()
    s1 = re.sub('[^a-z0-9]', '', s.lower())
    return s1 == s1[::-1]


print(isPalindrome("asdfg/'hjkl;;lkjg,./fdsa"))

# def isPalindrome(s):
#     s1 = s.lower()
#     li = list(s1)
#     for i in range(len(li)):
#         if ord(li[i]) < 48 or 57 < ord(li[i]) < 97 or ord(li[i]) > 122:
#             li[i] = ''
#     s2 = ''.join([str(d) for d in li])
#     print(s2)
#     return s2 == s2[::-1]

# def isPalindrome(x):
#     if x < 0:
#         return False
#     else:
#         str1 = str(x)
#         str2 = str1[::-1]
#         print(str1, str2)
#         return str1 == str2
#
#
# print(isPalindrome(1234321))


# def isPalindrome(x):
#     if x < 0:
#         return False
#     else:
#         li = list(int(a) for a in str(x))
#         j = int(len(li)/2)
#         k = 0
#         for i in range(j):
#             if li[i] != li[len(li)-1-i]:
#                 return False
#             else:
#                 k += 1
#         if k == j:
#             return True
