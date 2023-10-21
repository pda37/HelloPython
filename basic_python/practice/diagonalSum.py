def diagonalSum(mat):
    n = len(mat)
    ans = 0
    for i in range(n):
        if i != n-1-i:
            ans += mat[i][i] + mat[i][n-1-i]
        else:
            ans += mat[i][i]
    return ans


print(diagonalSum([[1,1,1],[1,1,1],[1,1,1]]))