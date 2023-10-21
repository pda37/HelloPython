def findPoisonedDuration(timeSeries, duration):
    if len(timeSeries) == 1:
        return duration
    else:
        time = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1] - timeSeries[i] >= duration:
                time += duration
            else:
                time += (timeSeries[i+1] - timeSeries[i])
        time += duration
        return time


print(findPoisonedDuration([33, 234], 23434))
