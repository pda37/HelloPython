def numWaterBottles(numBottles, numExchange):
    empty_bottles = 0
    ans = 0
    while numBottles > 0:
        ans += numBottles
        empty_bottles += numBottles
        numBottles = 0
        while empty_bottles >= numExchange:
            numBottles += int(empty_bottles / numExchange)
            empty_bottles -= numBottles * numExchange
    return ans


print(numWaterBottles(5, 5))