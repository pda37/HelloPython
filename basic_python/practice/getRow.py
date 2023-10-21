def getRow(rowIndex):
    # 0=<rowIndex<=33
    li = [[1]]
    for i in range(rowIndex):
        li[i].insert(0, 0)
        li[i].append(0)
        li.append([])
        for j in range(len(li[i])-1):
            li[i+1].append(li[i][j]+li[i][j+1])
    return li[rowIndex]


print(getRow(9))

