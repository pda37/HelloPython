def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]
    else:
        b = 0
        short = len(strs[0])
        for i in range(len(strs)-1):
            short = min(short, len(strs[i+1]))
        if short == 0:
            return ''
        else:
            for j in range(short):
                a = 1
                for m in range(len(strs)-1):
                    if strs[m][j] == strs[m+1][j]:
                        a += 1
                if a == len(strs):
                    b += 1
                else:
                    break
            print(strs, short, b, strs[0][0:b])
            return strs[0][0:b]
