def findContentChildren(g, s):
    g.sort()
    s.sort()
    n = 0
    for i in range(len(s)):
        if not g:
            break
        elif s[i] >= g[0]:
            g.pop(0)
            n += 1
    print(g, s, n)
    return n


print(findContentChildren([1, 2], [1, 2, 3]))
