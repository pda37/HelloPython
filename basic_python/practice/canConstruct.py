def canConstruct(ransomNote, magazine):
    a, b = {}, {}
    for r in ransomNote:
        if r in a:
            a[r] += 1
        else:
            a[r] = 1
    for m in magazine:
        if m in b:
            b[m] += 1
        else:
            b[m] = 1
    for r in a:
        if r not in b:
            return False
        elif b[r] < a[r]:
            return False
    return True


print(canConstruct('acdscs', 'csdcsacdsacds'))