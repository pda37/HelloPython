def checkPerfectNumber(num):
    if num == 1:
        return False
    else:
        a = 0
        i = 1
        while i < (int(num/i)+1):
            if num % i == 0:
                a += i + (num/i)
                i += 1
            else:
                i += 1
        return num == (a - num)


print(checkPerfectNumber(99999994))
