def isPathCrossing(path):
    a, b = 0, 0
    path_l = [[0, 0]]
    for i in range(len(path)):
        if path[i] == 'N':
            b += 1
        elif path[i] == 'S':
            b -= 1
        elif path[i] == 'E':
            a += 1
        elif path[i] == 'W':
            a -= 1
        if [a, b] not in path_l:
            path_l.append([a, b])
        else:
            return True
    return path_l


print(isPathCrossing("NES"))