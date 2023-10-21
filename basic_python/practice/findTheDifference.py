def findTheDifference(s, t):
    t_list = list(t)
    print(t_list)
    for a in s:
        if a in t_list:
            t_list.remove(a)
        else:
            return a
    return t_list[0]


print(findTheDifference('asdfgh', 'asdlfgh'))