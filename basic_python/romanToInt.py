# 罗马数字转整数
def romanToInt(roman):
    roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a = 0
    for i in range(0, len(roman)-1):
        if roman_int[roman[i]] >= roman_int[roman[i+1]]:
            a = a + roman_int[roman[i]]
        else:
            a = a - roman_int[roman[i]]
    a = a + roman_int[roman[-1]]
    return a


r = romanToInt('M')
print(r)


# class Solution:
#     def romanToInt(self, roman):
#         roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         a = 0
#         for i in range(0, len(roman)-1):
#             if roman_int[roman[i]] >= roman_int[roman[i+1]]:
#                 a = a + roman_int[roman[i]]
#             else:
#                 a = a - roman_int[roman[i]]
#         a = a + roman_int[roman[-1]]
#         return a
#
#
# r = Solution()
# b = r.romanToInt('M')
