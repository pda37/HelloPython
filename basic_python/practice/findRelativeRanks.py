def findRelativeRanks(score):
    score2 = sorted(score, reverse=True)
    ans = {}
    if len(score2) == 1:
        ans[score2[0]] = 'Gold Medal'
    elif len(score2) == 2:
        ans[score2[0]] = 'Gold Medal'
        ans[score2[1]] = 'Silver Medal'
    elif len(score2) >= 3:
        ans[score2[0]] = 'Gold Medal'
        ans[score2[1]] = 'Silver Medal'
        ans[score2[2]] = 'Bronze Medal'
        for i in range(3, len(score2)):
            ans[score2[i]] = str(i+1)
    score_order = []
    for s in score:
        print(s)
        score_order.append(ans[s])
    return score_order


print(findRelativeRanks([1,3,5,2,8,7]))
