def distanceBetweenBusStops(distance, start, destination):
    distance1, distance2 = 0, 0
    a = len(distance)
    distance.extend(distance)
    if start > destination:
        start, destination = destination, start
    for i in range(start, destination):
        distance1 += distance[i]
    for j in range(start + a, destination, -1):
        distance2 += distance[j - 1]
    return min(distance1, distance2)


print(distanceBetweenBusStops(distance=[1, 2, 3, 4], start=2, destination=2))