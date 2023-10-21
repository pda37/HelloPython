def convertToTitle(columnNumber):
    m = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = []
    while columnNumber > 26:
        ans.append(m[columnNumber % 26 - 1])
        if columnNumber % 26 == 0:
            columnNumber -= 26
        columnNumber = int(columnNumber/26)
    ans.append(m[columnNumber-1])
    return ''.join(ans[::-1])


print(convertToTitle(2147483647))