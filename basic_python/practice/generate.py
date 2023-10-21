def generate(numRows):
    # 1=<numRows<=30
    li = [[1]]
    for i in range(numRows-1):
        li[i].insert(0, 0)
        li[i].append(0)
        li.append([])
        for j in range(len(li[i])-1):
            li[i+1].append(li[i][j]+li[i][j+1])
    for i in range(numRows-1):
        li[i].pop()
        li[i].pop(0)
    return li


print(generate(10))
