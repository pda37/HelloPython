def decrypt(code, k):
    if k == 0:
        return [0]*len(code)
    else:
        length = len(code)
        code1 = []
        code.extend(code)
        s = 0
        if k > 0:
            for i in range(length):
                for j in range(i+1, i+k+1):
                    s += code[j]
                code1.append(s)
                s = 0
        else:
            for i in range(length):
                for j in range(length+i-1, length+i+k-1, -1):
                    s += code[j]
                code1.append(s)
                s = 0
    return code1


print(decrypt([5, 7, 1, 4], 3))