def numEquivDominoPairs(dominoes) -> int:
    dic = {}
    for i in range(len(dominoes)):
        if dominoes[i][0] > dominoes[i][1]:
            dominoes[i] = dominoes[i][::-1]
        if str(dominoes[i]) in dic:
            dic[str(dominoes[i])] += 1
        if str(dominoes[i]) not in dic:
            dic[str(dominoes[i])] = 1
    print(dic)
    ans = 0
    for k in dic:
        if dic[k] > 1:
            ans += dic[k]*(dic[k]-1)/2
    return ans


print(numEquivDominoPairs([[6, 7], [1, 2], [2, 1], [3, 4], [5, 6], [4, 3]]))

# def numEquivDominoPairs(dominoes):
#     if len(dominoes) == 1:
#         return 0
#     else:
#         a = 0
#         for i in range(len(dominoes)-1):
#             for j in range(i+1, len(dominoes)):
#                 if dominoes[i] == dominoes[j] or dominoes[i] == dominoes[j][::-1]:
#                     a += 1
#         return a
#
#
# print(numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6], [3, 4], [1, 2]]))
