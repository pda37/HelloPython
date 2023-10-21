def isIsomorphic(s: str, t: str):
    ans1 = {}
    ans2 = {}
    for i in range(len(s)):
        if s[i] not in ans1:
            ans1[s[i]] = t[i]
        else:
            if ans1[s[i]] != t[i]:
                return False
    for i in range(len(t)):
        if t[i] not in ans2:
            ans2[t[i]] = s[i]
        else:
            if ans2[t[i]] != s[i]:
                return False
    return True


print(isIsomorphic('qwer', 'ddgh'))