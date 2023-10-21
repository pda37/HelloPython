def distributeCandies(candyType):
    n = int(len(candyType)/2)
    ans = {}
    for candy in candyType:
        if candy in ans:
            ans[candy] += 1
        else:
            ans[candy] = 1
        if len(ans) >= n:
            return n
    if len(ans) >= n:
        return n
    else:
        return len(ans)


print(distributeCandies([1, 1, 1, 1]))
