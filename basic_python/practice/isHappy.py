def isHappy(n):
    happy = [n]
    i = 0
    m = 0
    while m != 1:
        li = list(int(a) for a in str(happy[i]))
        for j in range(len(li)):
            m += li[j]**2
        print(m)
        if m == 1:
            return True
        elif m in happy:
            return False
        else:
            happy.append(m)
            print(happy)
            i += 1
            m = 0


print(isHappy(68))
