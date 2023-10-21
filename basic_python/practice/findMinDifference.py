def findMinDifference(timePoints):
    ans = []
    for t in timePoints:
        a = int(t[0])*10*60 + int(t[1])*60 + int(t[3])*10 + int(t[4])
        ans.append(a)
    ans.sort()
    m = ans[0] - ans[-1] + 24*60
    for i in range(1, len(ans)):
        m = min(m, ans[i]-ans[i-1])
        if m == 0:
            return m
    return m


print(findMinDifference(["00:00", "23:59", "00:55"]))