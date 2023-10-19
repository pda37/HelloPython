# 整数反转输出
def reverse(num):
    if num == 0:
        return 0
    # elif num > (2**31-1) or num < -2**31:
    #     return 0
    else:
        dig = list(str(d) for d in str(num))  # 整数拆分成列表
        if num > 0:
            dig.reverse()
            num02 = int(''.join(dig))  # 将列表连接成字符串并转换成整数
            if num02 > (2**31-1):
                return 0
            else:
                return num02
        else:
            del dig[0]
            dig.reverse()
            num02 = int(''.join(dig))
            num03 = num02*(-1)
            if num03 < -2**31:
                return 0
            else:
                return num03


r = reverse(21474836)
print(r)
