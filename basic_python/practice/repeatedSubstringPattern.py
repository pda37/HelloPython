def repeatedSubstringPattern(s):
    n = len(s)
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            if s.count(s[0:i]) == int(n/i):
                return True
    return False


print(repeatedSubstringPattern('aba'))
