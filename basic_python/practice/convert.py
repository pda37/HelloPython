def convert(s, numRows):
    if numRows == 1:
        return s
    else:
        ans = []
        for i in range(numRows):
            ans.append([])
        for j in range(len(s)):
            remainder = j % (numRows*2-2)
            if remainder < numRows:
                ans[remainder].append(s[j])
                print(ans)
            else:
                remainder -= numRows-2
                ans[-remainder].append(s[j])
                print(ans)
        h = ''
        for k in range(numRows):
            h += ''.join(ans[k])
        return h


print(convert('Pqwerty.,,uiopasd,.fghjklzxcvbnm', 10))
