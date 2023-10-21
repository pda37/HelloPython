def isValid(s):
    if s == '':
        return False
    else:
        if (len(s) % 2) != 0:
            return False
        else:
            dic = {'(': -1, ')': 1, '{': -2, '}': 2, '[': -3, ']': 3}
            list_s = list(str(d) for d in s)
            if dic[list_s[0]] > 0:
                return False
            else:
                j = 1
                while len(list_s) > 2 and j < len(list_s):
                    if dic[list_s[0]] > 0:
                        return False
                    else:
                        j = 1
                        for i in range(len(list_s)-1):
                            if dic[list_s[i]] + dic[list_s[i+1]] == 0 and dic[list_s[i]] < dic[list_s[i+1]]:
                                list_s.pop(i)
                                list_s.pop(i)
                                break
                            else:
                                j += 1
                if not list_s or (dic[list_s[0]] + dic[list_s[1]] == 0 and dic[list_s[0]] < dic[list_s[1]]):
                    return True
                else:
                    return False


print(isValid("{}}{"))


# def isValid(s):
#     if s == '':
#         return False
#     else:
#         if (len(s) % 2) != 0:
#             return False
#         else:
#             while '()' in s or '{}' in s or '[]' in s:
#                 if s[0] == ')' or s[0] == '}' or s[0] == ']':
#                     print(s, s[0], 0)
#                     return False
#                 elif s[-1] == '(' or s[-1] == '{' or s[-1] == '[':
#                     print(s, s[-1], 1)
#                     return False
#                 else:
#                     s = s.replace('()', '')
#                     s = s.replace('{}', '')
#                     s = s.replace('[]', '')
#             print(s)
#             return s == ''
#
#
# print(isValid("{}"))