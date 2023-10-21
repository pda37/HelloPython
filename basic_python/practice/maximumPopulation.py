def maximumPopulation(logs):
    alive = {}
    for i in range(len(logs)):
        for j in range(logs[i][0], logs[i][1]):
            if j not in alive:
                alive[j] = 1
            else:
                alive[j] += 1
    print(alive)
    alive_order = sorted(alive.items(), key=lambda ali: (ali[1], -ali[0]), reverse=True)
    print(alive_order)
    return alive_order[0][0]


print(maximumPopulation([[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]))